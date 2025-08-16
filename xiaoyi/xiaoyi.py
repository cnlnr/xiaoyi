# xiaoyi/xiaoyi.py
import re, random, regex
import libcst as cst
import sys

def cli():
    args = sys.argv[1:]  # 跳过脚本名
    if len(args) == 0:
        print("""用法：
    xiaoyi file.xy           直接运行
    xiaoyi file.xy file.py   编译
源码：
    GitHub: https://github.com/cnlnr/xiaoyi
    Gitee: https://gitee.com/LZY4/xiaoyi""")
        sys.exit(1)
    elif len(args) == 1:
        code = open(args[0], encoding='utf-8').read()
        now_file = None
    elif len(args) == 2:
        code = open(args[0], encoding='utf-8').read()
        now_file = args[1]
    else:
        print("最多只能接受两个参数!")
        sys.exit(1)

    # 生成占位符
    def zwfhq():
        length = 1
        while True:
            zwf = "<" + ''.join(chr(random.randint(0x9FFF, 0x10FFFF)) for _ in range(length)) + ">"
            if zwf not in code:
                break
            length += 1
        return zwf

    # 使用两个独立的映射
    quote_map = {}
    bracket_map = {}

    def replace_quotes(m):
        full = m.group(0)
        key = zwfhq()
        quote_map[key] = full
        return key

    def replace_brackets(m):
        full = m.group(0)
        key = zwfhq()
        bracket_map[key] = full
        return key

    # 第一步：replace引号和注释
    quote_pattern = re.compile(r'''
        (?P<dquote>"[^"\\]*(?:\\.[^"\\]*)*")     # 双引号
        |
        (?P<squote>'[^'\\]*(?:\\.[^'\\]*)*')     # 单引号
        |
        (?P<comment>\#.*)                        # 注释
        |
        (?P<walrus>:=)                           # 海象
    ''', re.X)

    # 第一步replace后（引号和注释）
    processed = quote_pattern.sub(replace_quotes, code)


    # 第二步：replace大括号中和括号
    bracket_pattern = regex.compile(r'''
        (?P<brace>\{(?:[^{}]|(?P>brace))*\})         # 递归匹配大括号
        |
        (?P<square>\[(?:[^\[\]]|(?P>square))*\])     # 递归匹配中括号
    ''', re.X)

    # 第二步replace后（大括号中和括号）
    processed = bracket_pattern.sub(replace_brackets, processed)

    # 去除反斜杠换行
    processed = processed.replace("\\\n", "")

    # 编译保留关键字
    processed = processed.replace("导入", "import").replace("从", "from").replace("返回", "return").replace("跳出", "break").replace("@静态方法", "@staticmethod").replace("@类方法", "@classmethod")

    # 编译 class
    lines = processed.splitlines(True)
    out = []

    for line in lines:
        # 排除 if, else, try, except, finally, while, for, with 等关键字开头
        match = re.match(r'^(\s*)(?!\b(?:if|else|elif|try|except|finally|while|for|with|def|class)\b)(\w+)\s*:(.*)$', line)
        if match:
            indent, name, tail = match.groups()
            out.append(f"{indent}class {name}:{tail}\n")
        else:
            out.append(line)

    processed = ''.join(out)

    # 编译 def
    lines = processed.splitlines(True)
    out = []

    for line in lines:
        # 匹配任意缩进的函数定义，处理可选 async 前缀
        match = re.match(
        r'^(\s*)(async\s+)?(\w+)\s*(\(.*\))\s*:(.*)$',
        line
    )

        if match:
            indent, prefix, name, params, tail = match.groups()
            prefix = prefix or ''
            out.append(f"{indent}{prefix}def {name}{params}:{tail}\n")
        else:
            out.append(line)

    processed = ''.join(out)

    # 分阶段还原：先还原括号，再还原引号
    sorted_brackets = sorted(bracket_map.items(), key=lambda x: len(x[0]), reverse=True)
    for key, original in sorted_brackets:
        processed = processed.replace(key, original)

    sorted_quotes = sorted(quote_map.items(), key=lambda x: len(x[0]), reverse=True)
    for key, original in sorted_quotes:
        processed = processed.replace(key, original)

    # 定义函数名映射
    func_map = {
        "打印": "print",
        "输入": "input",
        # 可以继续添加更多函数名映射
    }

    # 定义属性名映射
    attr_map = {
        "替换": "replace",
        # 可以继续添加更多属性名映射
    }

    class RenameVisitor(cst.CSTTransformer):
        # 替换函数名
        def leave_Name(self, original_node, updated_node):
            if original_node.value in func_map:
                return updated_node.with_changes(value=func_map[original_node.value])
            return updated_node

        # 替换属性名
        def leave_Attribute(self, original_node, updated_node):
            if original_node.attr.value in attr_map:
                return updated_node.with_changes(attr=cst.Name(attr_map[original_node.attr.value]))
            return updated_node

    module = cst.parse_module(processed)
    code = module.visit(RenameVisitor()).code

    if now_file:  # 有文件名 → 写文件
        with open(now_file, "w", encoding="utf-8") as f:
            f.write(code)
    else:         # 没有文件名 → 直接执行
        exec(code)

# 支持直接运行脚本
if __name__ == "__main__":
    cli()
