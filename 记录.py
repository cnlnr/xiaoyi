import re

# 只在“函数头”行加 def：行首缩进 + 可选 async + 函数名 + 多行参数 + ) :
# 说明：
# - (?m)(?s) 打开 MULTILINE + DOTALL（让 . 可以跨行）
# - name 用 \w（已支持中文），若你担心可换成更严的：(?P<name>[^\W\d]\w*)
pattern = re.compile(
    r'(?ms)^(?P<indent>\s*)(?P<prefix>async\s+)?(?P<name>\w+)\s*'      # 缩进/async/函数名
    r'(?P<sig>\((?:.|\n)*?\))\s*'                                      # 多行参数: ... )
    r':(?P<tail>[^\n]*)$'                                              # 后跟冒号直到行末（可有注释）
)

def _repl(m):
    indent  = m.group('indent')
    prefix  = m.group('prefix') or ''
    name    = m.group('name')
    sig     = m.group('sig')
    tail    = m.group('tail')
    # 只在函数名前插入 "def "，其余一切保持不变
    return f"{indent}{prefix}def {name}{sig}:{tail}\n"

processed = pattern.sub(_repl, processed)











import regex  # pip install regex

pattern = regex.compile(
    r'(?ms)^(?P<indent>\s*)(?P<prefix>async\s+)?'
    r'(?P<name>[\p{L}_][\p{L}\p{N}_]*)\s*'       # 允许中文等所有字母类作为标识符
    r'(?P<sig>\((?:[^()]++|(?0))*\))\s*'         # 递归配平括号
    r':(?P<tail>[^\n]*)$'
)

def _repl(m):
    return f"{m.group('indent')}{m.group('prefix') or ''}def {m.group('name')}{m.group('sig')}:{m.group('tail')}\n"

processed = pattern.sub(_repl, processed)
