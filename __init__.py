from .modify_string_node import ModifyStringNode
from .show_string_node import ShowStringNode  

NODE_CLASS_MAPPINGS = {
    "ModifyStringNode": ModifyStringNode,
    "ShowStringNode": ShowStringNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ModifyStringNode": "Modify String",
    "ShowStringNode": "Show String",
}

WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]