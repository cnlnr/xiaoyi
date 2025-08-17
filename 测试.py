#!/usr/bin/env python3
import regex as re   # pip install regex

def compile_functions(src: str) -> str:
    pattern = re.compile(
        r"""(?smx)^([ \t]*)                     # 行首空白
        (async\s+)?                             # 1. 可选 async
        (\w+)                                   # 2. 真正的函数名
        (                                       # 3. 括号+类型+冒号
            \s*(?&b)\s*
            (?:\s*->[\s\S]*?)?
            \s*:
        )
        (?(DEFINE)(?<b>\((?:[^()]++|(?&b))*\)))
        """,
    )
    return pattern.sub(r'\1\2def \3\4', src)

# ---------------- 测试 ----------------
if __name__ == "__main__":
    processed = """
# 1. 顶层 async 函数
async  fetch(
    url: str,
    session=(await get_session()),
    timeout=10,
) -> dict[str, Any] | None:
    ...

# 2. 顶层普通函数
outer(
    x: int,
    y: list[tuple[int, str]]
) -> None:
    # 2.1 嵌套函数（无类型）
    inner():
        ...

    # 2.2 嵌套 async 函数
    async  nested_async(
        a=(
            b + c
        )
    ) -> int:
        return 42

    # 2.3 再嵌套一层
        deepest():
            ...

# 3. 类作用域
class  Foo:

    # 3.1 类方法
    cls_method(cls, data: bytes):
        ...

    # 3.2 静态方法
    static  create(
        a: int
    ) -> "Foo":
        ...

    # 3.3 实例 async 方法
    async  instance(
        self,
        payload: dict[str, Any]
    ):
        ...

    # 3.4 类内部再嵌套函数
    def outer_in_class(self):
        helper(
            x=1,
            y=(2, 3)
        ):
            ...
"""
    print("=== before ===")
    print(processed)

    processed = compile_functions(processed)

    print("=== after ===")
    print(processed)