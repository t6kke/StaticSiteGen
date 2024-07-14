from textnode import *
from htmlnode import *
from block_markdown import *
from inline_markdown import *


def markdown_to_html_node(markdown):
    
    final_HTMLnode_list = []
    block_list = markdown_to_blocks(markdown)

    for block in block_list:
        block_type = block_to_block_type(block)
        #print(block_type)
        if block_type == block_type_heading:
            h_nbr, h_text = get_heading_elements(block)
            heading_HTMLnode = LeafNode(f"h{h_nbr}", h_text)
            final_HTMLnode_list.append(heading_HTMLnode)
            #print(heading_HTMLnode)
        if block_type == block_type_paragraph:
            htmlnode_list = get_paragraph_html_nodes(block)
            paragraph_HTMLnode = ParentNode("p", htmlnode_list)
            final_HTMLnode_list.append(paragraph_HTMLnode)
            #print(paragraph_HTMLnode)
        if block_type == block_type_code:
            children = []
            code_html_node = get_code_leafnode(block)
            children.append(code_html_node)
            code_parent_HTMLnode = ParentNode("pre", children)
            final_HTMLnode_list.append(code_parent_HTMLnode)
            #print(code_parent_HTMLnode)
        if block_type == block_type_quote:
            clean_text = get_quote_text(block)
            quote_HTMLnode = LeafNode("blockquote", clean_text)
            final_HTMLnode_list.append(quote_HTMLnode)
            #print(quote_HTMLnode)
        if block_type == block_type_unordered_list:
            children = []
            children = make_lists_to_nodes(block)
            list_parent_HTMLnode = ParentNode("ul", children)
            final_HTMLnode_list.append(list_parent_HTMLnode)
            #print(list_parent_HTMLnode)
        if block_type == block_type_ordered_list:
            children = []
            children = make_lists_to_nodes(block)
            list_parent_HTMLnode = ParentNode("ol", children)
            final_HTMLnode_list.append(list_parent_HTMLnode)
            #print(list_parent_HTMLnode)

    #print(final_HTMLnode_list)
    final_HTMLnode = ParentNode("div", final_HTMLnode_list)
    return final_HTMLnode



def get_heading_elements(block):
    split_heading = block.split(" ", 1)
    heading_tag_nbr = len(split_heading[0])
    heading_text = split_heading[1]
    return heading_tag_nbr, heading_text

def get_paragraph_html_nodes(block):
    htmlnode_list = []
    textnode_list = text_to_textnodes(block)
    for node in textnode_list:
        htmlnode_list.append(text_node_to_html_node(node))
    return htmlnode_list

def get_code_leafnode(block):
    code_text = block.strip("```")
    code_text_node = TextNode(code_text, text_type_code)
    code_html_node = text_node_to_html_node(code_text_node)
    return code_html_node

def get_quote_text(block):
    clean_text = block.replace(">", "")
    #print(f"quote cleanup: {clean_text}")
    return clean_text

def make_lists_to_nodes(block):
    text_node_list = []
    HTML_node_list = []
    lines = block.split("\n")
    for line in lines:
        split_line = line.split(" ", 1)
        children = text_to_children(split_line[1])
        HTML_node_list.append(ParentNode("li", children))
    return HTML_node_list

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children