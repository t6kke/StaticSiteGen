import unittest
from markdown_to_html import *


class TestBlockMarkdown(unittest.TestCase):

    # boot.dev tests

    '''def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )
'''







    # my tests
    def test_markdown_to_html_1(self):
        base_markdown = '''just text'''
        result = markdown_to_html_node(base_markdown)
        self.assertEqual(
            "LeafNode(<div>, [LeafNode(<p>, [LeafNode(None, just text, None)], None)], None)",
            f"{result}")


    def test_markdown_to_html_2(self):
        base_markdown = '''- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items'''
        result = markdown_to_html_node(base_markdown)
        self.assertEqual(
            "LeafNode(<div>, [LeafNode(<ul>, [LeafNode(<li>, [LeafNode(None, This is a list, None)], None), LeafNode(<li>, [LeafNode(None, with items, None)], None), LeafNode(<li>, [LeafNode(None, and , None), LeafNode(i, more, None), LeafNode(None,  items, None)], None)], None), LeafNode(<ol>, [LeafNode(<li>, [LeafNode(None, This is an , None), LeafNode(code, ordered, None), LeafNode(None,  list, None)], None), LeafNode(<li>, [LeafNode(None, with items, None)], None), LeafNode(<li>, [LeafNode(None, and more items, None)], None)], None)], None)",
            f"{result}")

    def test_markdown_to_html_3(self):
        base_markdown = '''# main heading

p1l1 just some regular text
p1l2 more regular text

p2l1 This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)

### sub heading

p3l1 This is **bolded** paragraph

p4l1 This is another paragraph with *italic* text and `code` here
p4l2 This is the same paragraph on a new line
p4l3 and a third one

>quoted sentences line
>quoted sentence ongoing
>quote final line
>           - some guy

* This is a list
* with items

```\nSELECT * FROM my_db WHERE id = 10\n```

1. result1
2. result2
3. result3

p5l1 Source: [boot.dev](https://boot.dev)'''
        result = markdown_to_html_node(base_markdown)
        self.assertEqual(
            '''LeafNode(<div>, [LeafNode(<h1>, main heading, None), LeafNode(<p>, [LeafNode(None, p1l1 just some regular text
p1l2 more regular text, None)], None), LeafNode(<p>, [LeafNode(None, p2l1 This is text with an , None), LeafNode(img, , {'src': 'https://i.imgur.com/zjjcJKZ.png', 'alt': 'image'})], None), LeafNode(<h3>, sub heading, None), LeafNode(<p>, [LeafNode(None, p3l1 This is , None), LeafNode(b, bolded, None), LeafNode(None,  paragraph, None)], None), LeafNode(<p>, [LeafNode(None, p4l1 This is another paragraph with , None), LeafNode(i, italic, None), LeafNode(None,  text and , None), LeafNode(code, code, None), LeafNode(None,  here
p4l2 This is the same paragraph on a new line
p4l3 and a third one, None)], None), LeafNode(<blockquote>, quoted sentences line
quoted sentence ongoing
quote final line
           - some guy, None), LeafNode(<ul>, [LeafNode(<li>, [LeafNode(None, This is a list, None)], None), LeafNode(<li>, [LeafNode(None, with items, None)], None)], None), LeafNode(<pre>, [LeafNode(code, 
SELECT * FROM my_db WHERE id = 10
, None)], None), LeafNode(<ol>, [LeafNode(<li>, [LeafNode(None, result1, None)], None), LeafNode(<li>, [LeafNode(None, result2, None)], None), LeafNode(<li>, [LeafNode(None, result3, None)], None)], None), LeafNode(<p>, [LeafNode(None, p5l1 Source: , None), LeafNode(a, boot.dev, {'href': 'https://boot.dev'})], None)], None)''',
            f"{result}")



if __name__ == "__main__":
    unittest.main()
