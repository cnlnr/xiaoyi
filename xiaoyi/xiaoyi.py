import cst_name
import re_class_def

def code(processed: str) -> str:

    # 定义关键字映射
    keywords_map = {
        "导入": "import",
        "从": "from",
        "返回": "return",
        "跳出": "break",
        "继续": "continue",
        "全局": "global",
        "非局部": "nonlocal",
        "@静态方法": "@staticmethod",
        "@类方法": "@classmethod",
    }

    processed = re_class_def.compile_chinese_code(processed, keywords_map)

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

    processed = cst_name.rename_identifiers(processed, func_map, attr_map)
    return processed