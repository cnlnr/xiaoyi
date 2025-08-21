# 小易中文编程语言

![PyPI - Version](https://img.shields.io/pypi/v/xiaoyi)
[![star](https://gitee.com/LZY4/xiaoyi/badge/star.svg?theme=white)](https://gitee.com/LZY4/xiaoyi/stargazers)
![GitHub Repo stars](https://img.shields.io/github/stars/cnlnr/xiaoyi)

小易编程语言（xiaoyi）是简化版的 Python 中文编程语言,可编译成 Python 源码。

## 发展

开发一门编程语言是一件非常非常困难的事情,虽然我已经实现了,但考虑到其他因素,如vscode插件,我决定将不会积极推送新的代码

这非常非常的困难,需要大量的精力和时间,如果你愿意介绍挑战,欢迎 Fork 😊

## 安装

```shell
pip install xiaoyi
```

## 快速入门

更多文档请查看 [docs](https://gitee.com/LZY4/xiaoyi/blob/main/docs) 目录

### 如何运行或编译代码

```shell
cnlnr@xiaoxin ~> xiaoyi
小易中文编程语言 v0.1.2
用法：
    xiaoyi file.xy           直接运行
    xiaoyi file.xy file.py   编译成 Python 源码
源码：
    GitHub: https://github.com/cnlnr/xiaoyi
    Gitee:  https://gitee.com/LZY4/xiaoyi
cnlnr@xiaoxin ~ [1]> 
```

### 定义函数

```python
问候():
    返回 f"你好，{输入("_" * 20 + "\r你的名字是:")}"

打印(问候())
```

### 定义类

```python
打招呼:
    @静态方法
    问候(名字 = "世界"):
        打印(f'你好，{名字}')

打招呼.问候()
```

语法对照表请参阅 [docs/中英语法对照.md](https://gitee.com/LZY4/xiaoyi/blob/main/docs/%E4%B8%AD%E8%8B%B1%E8%AF%AD%E6%B3%95%E5%AF%B9%E7%85%A7.md)

提示!可以使用 [Meson](https://github.com/mesonbuild/meson) ,[make](https://www.make.com/),[ninja](https://github.com/ninja-build/ninja) 来编译你的项目

使用双拼可获得更快的打字速度

## 社区

点击链接加入腾讯频道【AI &小易编程语言社区 】：<https://pd.qq.com/s/dvvy24tpn?b=9>

## 赞助

[点我捐赠](jkm.jpeg)
