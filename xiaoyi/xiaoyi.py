import sys


def cli():
    args = sys.argv[1:]  # 跳过脚本名
    if len(args) == 0:
        print("""\
小易中文编程语言 v0.1.2
用法：
    xiaoyi file.xy           直接运行
    xiaoyi file.xy file.py   编译成 Python 源码
源码：
    GitHub: https://github.com/cnlnr/xiaoyi
    Gitee:  https://gitee.com/LZY4/xiaoyi""")
        sys.exit(1)
    elif len(args) == 1:
        code = open(args[0], encoding="utf-8").read()
        now_file = None
    elif len(args) == 2:
        code = open(args[0], encoding="utf-8").read()
        now_file = args[1]
    else:
        print("最多只能接受两个参数!")
        sys.exit(1)



    # 定义函数名映射
    func_map = {
        "打印": "print",
        "输入": "input",
        "范围": "range",
        "打开": "open",
        "退出": "exit",
    }

    # 定义属性名映射
    attr_map = {
        "替换": "replace",
        # 可以继续添加更多属性名映射
    }

    if now_file:  # 有文件名 → 写文件
        with open(now_file, "w", encoding="utf-8") as f:
            f.write(code)
    else:         # 没有文件名 → 直接执行
        import subprocess
        exit(subprocess.run([sys.executable, "-c", code], stdout=sys.stdout).returncode)


# 支持直接运行脚本
if __name__ == "__main__":
    cli()
