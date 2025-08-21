import cst_name
import re_class_def
from config import *

def code(processed: str) -> str:

    processed = re_class_def.compile_chinese_code(processed, keywords_map)
    processed = cst_name.rename_identifiers(processed, func_map, attr_map)
    return processed
