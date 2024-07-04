import unittest
from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    # boot.dev tests
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
    
    
    
    
    # personal tests 
    def test_eq_leafwithlink(self):
        node = LeafNode("div", "some text", {"class": "greeting", "href": "https://boot.dev"})
        self.assertEqual(node.to_html(), "<div class=\"greeting\" href=\"https://boot.dev\">some text</div>")

    def test_to_html_props(self):
        node = HTMLNode("div", "Hello world", None, {"class": "greeting", "href": "https://boot.dev"})
        self.assertEqual(node.props_to_html(), ' class="greeting" href="https://boot.dev"')

    #def test_eq(self):
        #node = HTMLNode("p", "text", "div", {"class": "greeting", "href": "https://boot.dev"})
        #node2 = HTMLNode("p", "text", "div", {"class": "greeting", "href": "https://boot.dev"})
        #self.assertEqual(node, node2)

    #def test_eq_none(self):
        #node = HTMLNode()
        #node2 = HTMLNode()
        #self.assertEqual(node, node2)

    def test_noteq(self):
        node = HTMLNode("tag", "value", "children")
        node2 = HTMLNode("tag", "value", "chasdfildren")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        tn = HTMLNode("tag", "value", "children", "props")
        self.assertEqual("HTMLNode(tag, value, children, props)", repr(tn))


if __name__ == "__main__":
    unittest.main()
