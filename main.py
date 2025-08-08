import re, random, string

code = '''
print('ab"卡斯丹房劳瑟丹"c')
print("ab'lg\\'lg\\\"iyguiyfi'c")
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

# 正确的正则表达式（使用原始字符串）
pattern = re.compile(r'''
    (?P<dquote>"[^"\\]*(?:\\.[^"\\]*)*")     # 双引号
    |
    (?P<squote>'[^'\\]*(?:\\.[^'\\]*)*')     # 单引号
    |
    (?P<comment>\#.*)                        # 注释
''', re.X)

processed = pattern.sub(replace, code)
print('替换后：')
print(processed)

# 统一还原
for key, original in placeholder_map.items():
    processed = processed.replace(key, original)

print('最终还原后：')
print(processed)