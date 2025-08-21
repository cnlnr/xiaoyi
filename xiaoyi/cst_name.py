import libcst as cst

def rename_identifiers(processed: str, func_map: dict, attr_map: dict) -> str:
    """替换函数名和属性名。"""
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

    module = cst.parse_module(processed)
    return module.visit(RenameVisitor()).code
