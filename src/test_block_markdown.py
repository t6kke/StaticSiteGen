import unittest
from block_markdown import *

class TestBlockMarkdown(unittest.TestCase):

    # boot.dev tests
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        block_type = block_to_block_type(block)
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)















    # my tests
    def test_markdown_split_eq1(self):
        base_markdown = '''just text'''
        blocked_text_list = markdown_to_blocks(base_markdown)
        self.assertListEqual(
            [
                "just text",
            ],
            blocked_text_list)
    
    def test_markdown_split_eq2(self):
        base_markdown = '''just text
        '''
        blocked_text_list = markdown_to_blocks(base_markdown)
        self.assertListEqual(
            [
                "just text",
            ],
            blocked_text_list)

    def test_markdown_split_eq3(self):
        base_markdown = '''This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items'''
        blocked_text_list = markdown_to_blocks(base_markdown)
        self.assertListEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
            blocked_text_list)


    def test_markdown_split_eq4(self):
        base_markdown = '''This is **bolded** paragraph


This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line







* This is a list
* with items'''
        blocked_text_list = markdown_to_blocks(base_markdown)
        self.assertListEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
            blocked_text_list)


    def test_markdown_blocktype_eq1(self):
        base_markdown = '''just text'''
        blocked_text_list = markdown_to_blocks(base_markdown)
        block_type = block_to_block_type(blocked_text_list[0])
        self.assertEqual("paragraph",block_type)
    
    def test_markdown_blocktype_eq2(self):
        base_markdown = '''### heading'''
        blocked_text_list = markdown_to_blocks(base_markdown)
        block_type = block_to_block_type(blocked_text_list[0])
        self.assertEqual("heading",block_type_heading)
    
    def test_markdown_blocktype_eq3(self):
        base_markdown = '''```code```'''
        blocked_text_list = markdown_to_blocks(base_markdown)
        block_type = block_to_block_type(blocked_text_list[0])
        self.assertEqual("code",block_type_code)
    
    def test_markdown_blocktype_eq4(self):
        base_markdown = '''* item
* item2'''
        blocked_text_list = markdown_to_blocks(base_markdown)
        block_type = block_to_block_type(blocked_text_list[0])
        self.assertEqual("unordered_list",block_type_unordered_list)

    def test_markdown_blocktype_eq5(self):
        base_markdown = '''```code```'''
        blocked_text_list = markdown_to_blocks(base_markdown)
        block = "* my list\n* my items"
        block_type = block_to_block_type(block)
        self.assertEqual("unordered_list",block_type_unordered_list)


if __name__ == "__main__":
    unittest.main()
