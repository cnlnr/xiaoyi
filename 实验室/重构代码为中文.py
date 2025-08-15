import libcst as cst

class RenameVisitor(cst.CSTTransformer):
    def leave_Name(self, original_node, updated_node):
        if original_node.value == "打印":
            return updated_node.with_changes(value="print")
        return updated_node

code = """
打印(123)  # 调用打印函数
"""

module = cst.parse_module(code)
new_module = module.visit(RenameVisitor())

print(new_module.code)


