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


def split_nodes_image(old_nodes):
    result_nodes = []
    solo_image = False

    #print(f"working on {old_nodes}")
    for node in old_nodes:
        images_list = extract_markdown_images(node.text)
        original_text = node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        #print(f"extracted images list: {images_list}")
        #print(f"tuple doing split: {images_list[0]}")
        split_text = node.text.split(f"![{images_list[0][0]}]({images_list[0][1]})", 1)
        for item in split_text:
            #print(item)
            pass
        if split_text[0] != "" and split_text[1] != "":
            #print("!!! Adding condition for middle image")
            split_text.insert(1, "REPLACE_THIS_WITH_IMAGE")
        elif split_text[0] == "" and split_text[1] == "":
            solo_image = True
        for item in split_text:
            #print(item)
            pass
        #print(f"Strings split: {split_text}")
        split_nodes = []
        #print(f"lenght of string list: {len(split_text)}")
        for i in range(len(split_text)):
            #print(f"Item: {i} --- String for processing: {split_text[i]}")
            if split_text[i] == "" and i == 0:
                #print("added first item image")
                tn = TextNode(images_list[0][0], text_type_image, images_list[0][1])
                split_nodes.append(tn)
            elif solo_image == False and split_text[i] == "" and i == len(split_text)-1:
                #print("added last item image")
                tn = TextNode(images_list[0][0], text_type_image, images_list[0][1])
                split_nodes.append(tn)
            elif split_text[i] != "" and split_text[i] != "REPLACE_THIS_WITH_IMAGE":
                #print("added regular text if exists: " + split_text[i])
                tn = TextNode(split_text[i], text_type_text)
                split_nodes.append(tn)
            elif split_text[i] == "REPLACE_THIS_WITH_IMAGE":
                #print("added image in middle")
                tn = TextNode(images_list[0][0], text_type_image, images_list[0][1])
                split_nodes.append(tn)
        result_nodes.extend(split_nodes)
        #print(f"Result list: {result_nodes}")
    for i in range(len(result_nodes)):
        if "![" in result_nodes[i].text:
            #print("!!! Found another image that needs processing")
            tn = result_nodes.pop(i)
            result_nodes.extend(split_nodes_image([tn]))
    return result_nodes



def split_nodes_link(old_nodes):
    result_nodes = []
    solo_link = False

    #print(f"working on {old_nodes}")
    for node in old_nodes:
        link_list = extract_markdown_links(node.text)
        #print(f"extracted images list: {link_list}")
        #print(f"tuple doing split: {link_list[0]}")
        split_text = node.text.split(f"[{link_list[0][0]}]({link_list[0][1]})", 1)
        for item in split_text:
            #print(item)
            pass
        if split_text[0] != "" and split_text[1] != "":
            #print("!!! Adding condition for middle image")
            split_text.insert(1, "REPLACE_THIS_WITH_LINK")
        elif split_text[0] == "" and split_text[1] == "":
            solo_link = True
        for item in split_text:
            #print(item)
            pass
        #print(f"Strings split: {split_text}")
        split_nodes = []
        #print(f"lenght of string list: {len(split_text)}")
        for i in range(len(split_text)):
            #print(f"Item: {i} --- String for processing: {split_text[i]}")
            if split_text[i] == "" and i == 0:
                #print("added first item image")
                tn = TextNode(link_list[0][0], text_type_link, link_list[0][1])
                split_nodes.append(tn)
            elif solo_link == True and split_text[i] == "" and i == len(split_text)-1:
                #print("added last item image")
                tn = TextNode(link_list[0][0], text_type_link, link_list[0][1])
                split_nodes.append(tn)
            elif split_text[i] != "" and split_text[i] != "REPLACE_THIS_WITH_LINK":
                #print("added regular text if exists: " + split_text[i])
                tn = TextNode(split_text[i], text_type_text)
                split_nodes.append(tn)
            elif split_text[i] == "REPLACE_THIS_WITH_LINK":
                #print("added image in middle")
                tn = TextNode(link_list[0][0], text_type_link, link_list[0][1])
                split_nodes.append(tn)
        result_nodes.extend(split_nodes)
        #print(f"Result list: {result_nodes}")
    for i in range(len(result_nodes)):
        if "[" in result_nodes[i].text:
            #print("!!! Found another image that needs processing")
            tn = result_nodes.pop(i)
            result_nodes.extend(split_nodes_link([tn]))
    return result_nodes