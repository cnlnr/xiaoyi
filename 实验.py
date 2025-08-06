import re

# 提取双引号内的内容
text = '这是一个"示例"文本'
result = re.findall(r'"([^"]*)"', text)
print(result)  # 输出: ['示例']

# 提取单引号内的内容
text2 = '这是一个\'示例\'文本'
result2 = re.findall(r"'([^']*)'", text2)
print(result2)  # 输出: ['示例']

# 提取双引号
pattern = r'"(.*?)"'
results = re.findall(pattern, text)