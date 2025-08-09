import re, random, string, regex

code = open('实验.xy',  encoding='utf-8').read()


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












# 简化版行合并逻辑
# 简化后的核心处理逻辑
lines = processed.splitlines(True)
out = []
i = 0

while i < len(lines):
    if i+1 < len(lines):
        match = re.match(
            r'^(\s*)'
            r'(?!if|else|elif|for|while|try|except|finally|with|class|True|False)\b'

            r'(\S+)\s*:(.*)$',
            lines[i]
        )

        if match:
            indent, token, tail = match.groups()
            next_line = lines[i+1].lstrip()
            if next_line.startswith('('):
                param = next_line.split('\n', 1)[0]
                out.append(f"{indent}def {token}{param}:{tail}\n")
                i += 2
                continue
            else:
                out.append(f"{indent}def {token}():{tail}\n")
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

print("="*80)
print(processed)
print("="*80)
exec(processed)
