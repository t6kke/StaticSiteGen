from textnode import *

# my fuction
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result_nodes = []
    out_type = ""

    if delimiter == "**":
        out_type = text_type_bold
    elif delimiter == "*":
        out_type = text_type_italic
    elif delimiter == "`":
        out_type = text_type_code
    else:
        raise Exception("No valid delimiter provided")

    for node in old_nodes:
        if node.text_type != text_type_text:
            result_nodes.append(node)
            continue
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise Exception("Missing correct pairing of delimiters")
        index = 0
        for item in split_text:
            if len(item) > 0:
                if index % 2 == 0:
                    tn = TextNode(item, text_type_text)
                else:
                    tn = TextNode(item, out_type)
                result_nodes.append(tn)
            index += 1
    return result_nodes


# this is from boot.dev
def split_nodes_delimiter_example(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    result_list = []
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    result_list = []
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches