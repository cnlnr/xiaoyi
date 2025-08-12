import re, random, regex

code = open("/home/cnlnr/工作区/xiaoyi/main.xy",  encoding='utf-8').read()



# 生成占位符
def zwfhq():
    length = 1
    while True:
        zwf = "<" + ''.join(chr(random.randint(126, 0x10FFFF)) for _ in range(length)) + ">"
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

# 第一步：替换引号和注释
quote_pattern = re.compile(r'''
    (?P<dquote>"[^"\\]*(?:\\.[^"\\]*)*")     # 双引号
    |
    (?P<squote>'[^'\\]*(?:\\.[^'\\]*)*')     # 单引号
    |
    (?P<comment>\#.*)                        # 注释
    |
    (?P<walrus>:=)                           # 海象
''', re.X)

# 第一步替换后（引号和注释）
processed = quote_pattern.sub(replace_quotes, code)

# 第二步：替换大括号中和括号
bracket_pattern = regex.compile(r'''
    (?P<brace>\{(?:[^{}]|(?P>brace))*\})     # 递归匹配大括号
    |
    (?P<square>\[(?:[^\[\]]|(?P>square))*\])     # 递归匹配中括号
''', re.X)

# 第二步替换后（大括号中和括号）
processed = bracket_pattern.sub(replace_brackets, processed)










# 中文替换
zwyfc = {
    '假':'False',
    '无':'None',
    '真':'True',
    '与':'and',
    '别名':'as',
    '断言':'assert',
    '异步':'async',
    '等待':'await',
    '跳出':'break',
    '类':'class',
    '继续':'continue',
    '删除':'del',
    '再若':'elif',
    '否则':'else',
    '异常':'except',
    '最终':'finally',
    '为':'for',
    '从':'from',
    '全局':'global',
    '若':'if',
    '导入':'import',
    '在':'in',
    '是':'is',
    '非局部':'nonlocal',
    '非':'not',
    '或':'or',
    '引发':'raise',
    '返回':'return',
    '尝试':'try',
    '当':'while',
    '产出':'yield',
    '绝对值':'abs',
    '布尔':'bool',
    '跳出':'break',
    '可调用':'callable',
    '类方法':'classmethod',
    '编译':'compile',
    '复数':'complex',
    '删除属性':'delattr',
    '字典':'dict',
    '目录':'dir',
    '商余':'divmod',
    '枚举':'enumerate',
    '执行':'exec',
    '离开':'exit',
    '过滤器':'filter',
    '浮点数':'float',
    '格式化':'format',
    '不可变集合':'frozenset',
    '获取属性':'getattr',
    '全局变量':'globals',
    '是否有属性':'hasattr',
    '哈希':'hash',
    '帮助':'help',
    '十六进制':'hex',
    '标识':'id',
    '输入':'input',
    '整数':'int',
    # '':'isinstance',
    # '':'issubclass',
    # '':'iter',
    '个数':'len',
    # '':'license',
    '列表':'list',
    '本地变量':'locals',
    '映射':'map',
    '最大':'max',
    '内存视图':'memoryview',
    '最小':'min',
    '下一个':'next',
    '对象':'object',
    '八进制':'oct',
    '打开':'open',
    '有序对':'ord',
    '幂':'pow',
    '打印':'print',
    '属性':'property',
    '退出':'quit',
    '范围':'range',
    '表示':'repr',
    '反转':'reversed',
    '四舍五入':'round',
    '集合':'set',
    '设置属性':'setattr',
    '切片':'slice',
    '排序':'sorted',
    '静态方法':'staticmethod',
    '字符串':'str',
    '总和':'sum',
    '超类':'super',
    '元组':'tuple',
    '类型':'type',
    '变量':'vars',
    '压缩':'zip',
    '.替换':'.replace',



}
for k, v in zwyfc.items():
    processed = processed.replace(k, v)













# 编译函数
lines = processed.splitlines(True)
out = []
i = 0

while i < len(lines):
    if i+1 < len(lines):
        match = re.match(
            r'^(\s*)(async\s+)?(?!\b(?:else|try|finally|class|except)\b)(\w+)\s*:(.*)$',
            lines[i]
        )

        if match:
            indent, prefix, func, tail = match.groups()
            prefix = prefix or ''
            next_line = lines[i+1].lstrip()
            if next_line.startswith('('):
                param = next_line.split('\n', 1)[0]
                out.append(f"{indent}{prefix}def {func}{param}:{tail}\n")
                i += 2
                continue
            else:
                out.append(f"{indent}{prefix}def {func}():{tail}\n")
                i += 1
                continue
    out.append(lines[i])
    i += 1

processed = ''.join(out)














# 分阶段还原：先还原括号，再还原引号
sorted_brackets = sorted(bracket_map.items(), key=lambda x: len(x[0]), reverse=True)
for key, original in sorted_brackets:
    processed = processed.replace(key, original)

sorted_quotes = sorted(quote_map.items(), key=lambda x: len(x[0]), reverse=True)
for key, original in sorted_quotes:
    processed = processed.replace(key, original)

with open("/home/cnlnr/工作区/xiaoyi/build/main.py", 'w', encoding='utf-8') as file:
    file.write(processed)
