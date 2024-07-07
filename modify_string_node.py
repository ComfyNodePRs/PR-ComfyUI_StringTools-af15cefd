import re

class ModifyStringNode:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_string": ("STRING", {"forceInput": True}),
                "strings_to_remove": ("STRING", {"multiline": True, "placeholder": "Enter one of more words or strings to remove. Seperate multiple strings using commas."}),
                "strings_to_replace": ("STRING", {"multiline": True, "placeholder": "Type the string or word to be replaced seperated by a colon. Seperate multiple string replacements with commas. Example to replace the word dog with cat you would enter dog:cat"}),
                "case_sensitive": (["True", "False"], {"default": "False"})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output_modified_string",)
    FUNCTION = "modify_string"
    CATEGORY = "StringTools"

    def modify_string(self, input_string, strings_to_remove, strings_to_replace, case_sensitive):
        case_sensitive = case_sensitive == "True"

        # Convert strings_to_remove to a list
        strings_to_remove = [s.strip() for s in re.split(r'[\n,]', strings_to_remove) if s.strip()]
        
        # Convert replacements string to a dictionary
        replacements_dict = {}
        if strings_to_replace:
            pairs = [pair.strip() for pair in re.split(r'[\n,]', strings_to_replace) if pair.strip()]
            for pair in pairs:
                try:
                    key, value = pair.split(':')
                    replacements_dict[key.strip()] = value.strip()
                except ValueError:
                    print(f"Warning: Invalid replacement pair '{pair}'. Skipping.")

        # Remove strings
        for s in strings_to_remove:
            if case_sensitive:
                input_string = input_string.replace(s, '')
            else:
                input_string = re.sub(re.escape(s), '', input_string, flags=re.IGNORECASE)

        # Replace strings
        for old_string, new_string in replacements_dict.items():
            if case_sensitive:
                input_string = input_string.replace(old_string, new_string)
            else:
                input_string = re.sub(re.escape(old_string), new_string, input_string, flags=re.IGNORECASE)

        # Remove extra spaces
        input_string = re.sub(r'\s+', ' ', input_string).strip()
        
        # Clean up spaces around commas and ensure a space after each comma
        input_string = re.sub(r'\s*,\s*', ', ', input_string)
        
        # Remove space at the start of the string if it exists
        input_string = input_string.lstrip()
        
        return (input_string,)

NODE_CLASS_MAPPINGS = {
    "ModifyStringNode": ModifyStringNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ModifyStringNode": "Modify String",
}
