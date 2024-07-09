from textnode import *
from htmlnode import *
from inline_markdown import *
from block_markdown import *


text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


def main():

    #initial check
    tn1 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    #print(tn1)
    tn2 = TextNode("This is a text node", "bold")
    #print(tn2)


    #second check
    tn3 = TextNode("This is a `text` node", "text")
    tn4 = TextNode("This `is a text` node", "text")
    #tn5 = TextNode("This `is a text node", "text")
    tn6 = TextNode("`This is a text node`", "text")
    tn_list = [tn3, tn4, tn6]
    n_list = split_nodes_delimiter(tn_list, "`", text_type_code)
    #print(n_list)

    tn3 = TextNode("This is a *text* node", "text")
    tn4 = TextNode("This *is a text* node", "text")
    tn_list = [tn3, tn4]
    n_list2 = split_nodes_delimiter(tn_list, "*", text_type_italic)
    tn_list2 = [tn3, tn4]
    n_list = split_nodes_delimiter(tn_list2, "*", text_type_italic)
    #print(n_list)
    
    node = TextNode("**bold** and *italic*", text_type_text)
    new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
    new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
    #print(f"main {new_nodes}")

    text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
    #print(extract_markdown_images(text))

    text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    #print(extract_markdown_links(text))



    #third check
    node = TextNode(
    "This is text with an ![n1_image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![n1_second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    text_type_text,
    )
    node2 = TextNode(
    "![n2_image](https://storage.googleapis.com/zjjcJKZ.png) and ![n2_second image](https://storage.googleapis.com/3elNhQu.png)",
    text_type_text,
    )
    node3 = TextNode( "![image](https://www.example.com/image.png)",text_type_text,)
    #new_nodes = split_nodes_image([node3])
    #print(new_nodes)


    node = TextNode(
    "This is text with an [n1_link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [n1_second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    text_type_text,
    )
    node2 = TextNode(
    "[n2_link](https://storage.googleapis.com/zjjcJKZ.png) and [n2_link image](https://storage.googleapis.com/3elNhQu.png)",
    text_type_text,
    )
    #new_nodes = split_nodes_link([node, node2])
    #print(new_nodes)


    #fourth check
    text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
    new_nodes = text_to_textnodes(text)
    #print(new_nodes)


    # fifth checks
    base_markdown = '''This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items'''
    markdown_block_list = markdown_to_blocks(base_markdown)
    print(markdown_block_list)
    for item in markdown_block_list:
        print(block_to_block_type(item))

    base_markdown = '''### heading'''
    markdown_block_list = markdown_to_blocks(base_markdown)
    print(markdown_block_list)
    for item in markdown_block_list:
        print(block_to_block_type(item))

main()