class Demo:

    def greet(cls):
        print('Hello from', cls.__name__)

# 正确：加括号 → 执行
Demo.greet()          # 输出: Hello from Demo