import unittest
from block_handler import markdown_to_blocks, block_to_block_type, BlockType

class TestBlockHandler(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    def test_block2block_types_heading(self):
        md = "### Title3 "
        block_type_test = block_to_block_type(md)
        expected = BlockType.HEADING
        self.assertEqual(block_type_test, expected)


    def test_block2block_types_code(self):
        md = '''
```python
print("Hello world!")
```
'''
        block_type_test = block_to_block_type(md)
        expected = BlockType.CODE
        self.assertEqual(block_type_test, expected)

    def test_block2block_types_quote(self):
        md = '''
>Hehe
>Hahamster (c)
        '''
        block_type_test = block_to_block_type(md)
        expected = BlockType.QUOTE
        self.assertEqual(block_type_test, expected)

    def test_block2block_types_paragraph(self):
        md = "This is just a paragraph of text"
        block_type_test = block_to_block_type(md)
        expected = BlockType.PARAGRAPH
        self.assertEqual(block_type_test, expected)

    def test_block2block_types_ul(self):
        md = """
- carton of milk
- ketchup
- potatoes
"""
        block_type_test = block_to_block_type(md)
        expected = BlockType.UNORDERED_LIST
        self.assertEqual(block_type_test, expected)

    def test_block2block_types_ol(self):
        md = """
1. carton of milk
2. ketchup
3. potatoes
"""
        block_type_test = block_to_block_type(md)
        expected = BlockType.ORDERED_LIST
        self.assertEqual(block_type_test, expected)