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
    (?P<brace>\{(?:[^{}]|(?P>brace))*\})     # 递归匹配大括号
    |
    (?P<square>\[(?:[^\[\]]|(?P>square))*\])     # 递归匹配中括号
''', re.X)

# 第二步replace后（大括号中和括号）
processed = bracket_pattern.sub(replace_brackets, processed)

# 编译中文
processed = processed.replace("导入", "import").replace("从", "from").replace("返回", "return").replace("跳出", "break").replace("@staticmethod", "静态方法").replace("@classmethod", "类方法")









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
