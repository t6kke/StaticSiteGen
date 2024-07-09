from textnode import *

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"



def markdown_to_blocks(markdown):
    result_list = []
    markdown_list = markdown.split("\n\n")
    for item in markdown_list:
        if item == "":
            continue
        item = item.strip()
        result_list.append(item)
    return result_list

def block_to_block_type(block):
    if "\n" not in block:
        if re.match("^#{1,6} ", block):
            return block_type_heading
        if block.startswith("```") and block.endswith("```"):
            return block_type_code
        if block.startswith(">"):
            return block_type_quote
        if block.startswith("* ") or block.startswith("- "):
            return block_type_unordered_list
        if re.match("'^1+\. '", block):
            return block_type_ordered_list
    else:
        block_line_list = block.split("\n")
        if len(block_line_list) > 1 and block_line_list[0].startswith("```") and block_line_list[-1].startswith("```"):
            return block_type_code
        if block_line_list[0].startswith(">"):
            for line in block_line_list:
                if line.startswith(">"):
                    continue
                else:
                    return block_type_paragraph
            return block_type_quote
        if block_line_list[0].startswith("* ") or block_line_list[0].startswith("- "):
            for line in block_line_list:
                if line.startswith("* ") or line.startswith("- "):
                    continue
                else:
                    return block_type_paragraph
            return block_type_unordered_list
        counter = 1
        if re.match("^1+\. ", block_line_list[0]):
            for line in block_line_list:
                if re.match("^\d+\. ", line) and line[0] == str(counter):
                    counter += 1
                    continue
                else:
                    return block_type_paragraph
            return block_type_ordered_list

    return block_type_paragraph
    raise ValueError(f"No block type found")

    