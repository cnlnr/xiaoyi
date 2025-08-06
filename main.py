import random
import re

code = open('实验.xy', encoding='utf-8').read()


def ultimate_garbage(length):return ''.join(chr(random.randint(93, 0x10FFFF)) for _ in range(length))


def zwfhq():
    length = 1
    while True:
        zwf = ultimate_garbage(length)
        if zwf not in code:
            break
        length += 1
        print(length)
    return zwf


# 提取双引号内的内容
syh = re.findall(r'"((?:[^"\\]|\\.)*)"', code)

# 提取单引号内的内容
dyh = re.findall(r"'((?:[^'\\]|\\.)*)'", code)

# 提取注释
comment = re.findall(r'#.*', code)


print(code)
