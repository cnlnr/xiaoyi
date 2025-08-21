import sys
import re_class_def
from config import *

def cli():
    help_str = "用法：xiaoyi-py file.py file.xy  编译成 Xiaoyi 源码"
    args = sys.argv[1:]  # 跳过脚本名
    if len(args) == 0:
        print(help_str)
        sys.exit(1)

    elif len(args) == 1:
        print(help_str)
        sys.exit(1)

    elif len(args) == 2:
        code = open(args[0], encoding="utf-8").read()
        now_file = args[1]
    else:
        print("最多只能接受两个参数!")
        sys.exit(1)

    code = re_class_def.compile_chinese_code.zwfhq(code).replace("class ", "").replace("def ", "")


    with open(now_file, "w", encoding="utf-8") as f:
        f.write(code)
