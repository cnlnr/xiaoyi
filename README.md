# 小易

编写简易的编程语言，与 Python 紧密结合,支持中文编程。

## 安装

```shell
pip install xiaoyi
```

## 发展

由于一些原因使得项目的进展异常的困难, ~~我可能不会积极改进这些费解的bug,~~ 如果你愿意接受挑战,欢迎Fork

## 快速入门

更多文档请查看 [docs](docs) 目录

### 如何运行或编译代码

```shell
cnlnr@xiaoxin ~> xiaoyi
用法：
    xiaoyi file.xy           直接运行
    xiaoyi file.xy file.py   编译
源码：
    GitHub: https://github.com/cnlnr/xiaoyi
    Gitee: https://gitee.com/LZY4/xiaoyi
cnlnr@xiaoxin ~ [1]> 
```

### 定义函数


```python
问候():
    打印('你好')
```

也可以这样写

```python
问候\
    (名字 = "世界"):
    打印(f'你好，{名字}')

问候()
```

### 定义类

```python
打招呼:
    @静态方法
    问候(名字 = "世界"):
        打印(f'你好，{名字}')

打招呼.问候()
```

提示!可以使用 [Meson](https://github.com/mesonbuild/meson) ,[make](https://www.make.com/),[ninja](https://github.com/ninja-build/ninja) 来编译你的项目


## Bug

- 语法糖内的保留关键字无法是中文

- exec 的代码不会自动转换成python代码
