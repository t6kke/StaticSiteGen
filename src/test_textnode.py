import unittest

from textnode import *
from inline_markdown import *


class TestTextNode(unittest.TestCase):
    # boot.dev tests








    # personal tests 1
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_noteq_notype(self):
        node = TextNode("This is a text node", "")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_noteq_urlNone(self):
        node = TextNode("This is a text node", "bold", "None")
        node2 = TextNode("This is a text node", "bold", None)
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        tn = TextNode("This is a text node", "")
        self.assertEqual("TextNode(This is a text node, "", "+str(None)+")", repr(tn))
    
    # personal tests 2 --- something is bad with comparsion data is the same
    def test_split_eq(self):
        tn3 = TextNode("This is a `text` node", "text")
        tn4 = TextNode("This `is a text` node", "text")
        tn5 = TextNode("`This is a text node`", "text")
        tn_list = [tn3, tn4, tn5]
        n_list = split_nodes_delimiter(tn_list, "`", text_type_code)
        #print(f"TEST!!! --- {n_list} /n")
        self.assertEqual([TextNode("This is a ", text_type_text, None), TextNode("text", text_type_code, None), TextNode(" node", text_type_text, None), TextNode("This ", text_type_text, None), TextNode("is a text", text_type_code, None), TextNode(" node", text_type_text, None), TextNode("This is a text node", text_type_code, None)], n_list)
    
    def test_split2_eq(self):
        tn3 = TextNode("This is a *text* node", "text")
        tn4 = TextNode("This *is a text* node", "text")
        tn_list = [tn3, tn4]
        n_list = split_nodes_delimiter(tn_list, "*", text_type_italic)
        #print(f"TEST!!! --- {n_list} /n")
        self.assertEqual([TextNode("This is a ", text_type_text, None), TextNode("text", text_type_italic, None), TextNode(" node", text_type_text, None), TextNode("This ", text_type_text, None), TextNode("is a text", text_type_italic, None), TextNode(" node", text_type_text, None)], n_list)

    def test_image_eq(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        image_list = extract_markdown_images(text)
        self.assertEqual([('image', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png'), ('another', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png')], image_list)

    def test_link_eq(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        link_list = extract_markdown_links(text)
        self.assertEqual([('link', 'https://www.example.com'), ('another', 'https://www.example.com/another')], link_list)

if __name__ == "__main__":
    unittest.main()
