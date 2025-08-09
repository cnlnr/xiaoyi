import re, random, string, regex

code = '''
# 列表例子
这是一个列表例子：[1, 2, 3, 4, 5] # 这是一个列表例子：
这里有一个嵌套列表：[[1, 2], [3, 4], [5, 6]]"hello"
混合类型列表：[1, "hello", 3.14, True]
这是一个字典例子：{"name": "Alice", "age": 25, "city": "New York"}
嵌套字典：{"person": {"name": "Bob", "age": 30}, "job": "Engineer"}
'''

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
''', re.X)

processed = quote_pattern.sub(replace_quotes, code)
print('第一步替换后（引号和注释）：')
print(processed)

# 第二步：替换大括号和中括号
bracket_pattern = regex.compile(r'''
    (?P<brace>\{(?:[^{}]|(?P>brace))*\})     # 递归匹配大括号
    |
    (?P<square>\[(?:[^\[\]]|(?P>square))*\])     # 递归匹配中括号
''', re.X)

processed = bracket_pattern.sub(replace_brackets, processed)
print('第二步替换后（大括号和中括号）：')
print(processed)

# 分阶段还原：先还原括号，再还原引号
sorted_brackets = sorted(bracket_map.items(), key=lambda x: len(x[0]), reverse=True)
for key, original in sorted_brackets:
    processed = processed.replace(key, original)

sorted_quotes = sorted(quote_map.items(), key=lambda x: len(x[0]), reverse=True)
for key, original in sorted_quotes:
    processed = processed.replace(key, original)

print('最终还原后：')
print(processed)





