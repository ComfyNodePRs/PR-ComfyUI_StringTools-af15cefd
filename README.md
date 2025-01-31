# ComfyUI_StringTools

Custom nodes for ComfyUI enhances functionality by allowing string modifications. Supports operations such as substring removal and replacement with other substrings. Useful for altering prompts and outputs generated by large language models (LLMs), enabling refinement of text outputs.

## ModifyStringNode

`Add Node > StringTools > Modify String`  

![node_example](modify_string_node.png)

**Note:** You may need to drag and resize the `Modify String` node on first use to see all the text and options. 

## ShowStringNode

A simple node to display a string in the node itself. To see the changes made made by the above Modify String node your could link the `output_string` to the `input_string` of the Show String node.

`Add Node > StringTools > Show String`  

![node_example](show_string_node.png)


## Usage example
![node_example](node_usage_example.png)

## Installation

```terminal
# Change to the directory you installed ComfyUI
cd pathTo/ComfyUI

# Change to the custom_nodes directory ie.
cd custom_nodes

# Clone the repo into custom_nodes
git clone https://github.com/bradsec/ComfyUI_StringTools.git

# Restart ComfyUI
```

