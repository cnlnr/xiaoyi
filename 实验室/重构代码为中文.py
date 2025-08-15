import libcst as cst

# 定义函数名映射
func_map = {
    "打印": "print",
    "输入": "input",
    # 可以继续添加更多函数名映射
}

# 定义属性名映射
attr_map = {
    "替换": "replace",
    # 可以继续添加更多属性名映射
}

class RenameVisitor(cst.CSTTransformer):
    # 替换函数名
    def leave_Name(self, original_node, updated_node):
        if original_node.value in func_map:
            return updated_node.with_changes(value=func_map[original_node.value])
        return updated_node

    # 替换属性名
    def leave_Attribute(self, original_node, updated_node):
        if original_node.attr.value in attr_map:
            return updated_node.with_changes(attr=cst.Name(attr_map[original_node.attr.value]))
        return updated_node

code = """
a = "hello"
打印(f"{a.替换("h", "H")}")
输入()
"""

module = cst.parse_module(code)
new_module = module.visit(RenameVisitor())

print(new_module.code)
