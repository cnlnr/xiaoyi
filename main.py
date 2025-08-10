import re, random, regex

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










# 中文替换
zwyfc = {

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
            
            # 查找参数块
            param_lines = []
            j = i + 1
            found_start = False
            found_end = False
            
            while j < len(lines):
                line = lines[j]
                if not found_start and line.strip().startswith('('):
                    found_start = True
                    param_lines.append(line)
                    if ')' in line:
                        found_end = True
                        break
                elif found_start and not found_end:
                    param_lines.append(line)
                    if ')' in line:
                        found_end = True
                        break
                elif found_start and found_end:
                    break
                else:
                    break
                j += 1
            
            if found_start and found_end:
                # 合并参数行
                full_param = ''.join(param_lines).strip()
                out.append(f"{indent}{prefix}def {func}{full_param}:\n")
                i = j + 1
                continue
            else:
                out.append(f"{indent}{prefix}def {func}():\n")
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

with open('实验.py', 'w', encoding='utf-8') as file:
    file.write(processed)
