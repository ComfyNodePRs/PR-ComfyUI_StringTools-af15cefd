class ShowStringNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input_string": ("STRING", {"forceInput": True}),
            },
            "hidden": {},
        }

    INPUT_IS_LIST = True  # Allows the node to accept a list of inputs
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output_string",)
    FUNCTION = "show_string"
    OUTPUT_NODE = True
    CATEGORY = "StringTools"

    def show_string(self, input_string):
        # Returns a dictionary with UI update info and the result
        return {"ui": {"text": input_string}, "result": (input_string,)}

NODE_CLASS_MAPPINGS = {
    "ShowStringNode": ShowStringNode
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "ShowStringNode": "Show String Node"
}