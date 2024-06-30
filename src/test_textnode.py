import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()
