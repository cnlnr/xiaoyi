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

# 统一的占位符映射
placeholder_map = {}

def replace(m):
    full = m.group(0)
    key = zwfhq()
    placeholder_map[key] = full
    return key

# 第一步：处理引号和注释
pattern = re.compile(r'''
    (?P<dquote>"[^"\\]*(?:\\.[^"\\]*)*")     # 双引号
    |
    (?P<squote>'[^'\\]*(?:\\.[^'\\]*)*')     # 单引号
    |
    (?P<comment>\#.*)                        # 注释
''', re.X)

processed = pattern.sub(replace, code)
print('第一步替换后（引号和注释）：')
print(processed)

# 第二步：处理大括号和中括号（跳过已存在的占位符）
brace_pattern = regex.compile(r'''
    (?P<brace>\{(?:[^{}]|(?P>brace))*\})     # 递归匹配大括号
    |
    (?P<square>\[(?:[^\[\]]|(?P>square))*\])     # 递归匹配中括号
''', re.X)

# 修改replace函数，避免替换已存在的占位符
original_replace = replace
def replace_bracket(m):
    full = m.group(0)
    # 检查是否包含已存在的占位符
    for key in placeholder_map:
        if key in full:
            return full  # 如果包含占位符，不替换
    return original_replace(m)

processed = brace_pattern.sub(replace_bracket, processed)
print('第二步替换后（大括号和中括号）：')
print(processed)

# 统一还原
for key, original in placeholder_map.items():
    processed = processed.replace(key, original)

print('最终还原后：')
print(processed)





