import unittest
from textnode import TextNode, TextType
from text_nodes_handler import split_nodes_delimiter

class Test_TextNodesHandler(unittest.TestCase):
    def test_bold(self):
        new_node = TextNode("This is text with a **bolded phrase** in the middle",TextType.TEXT)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT),
            ]
        output = split_nodes_delimiter([new_node],"**", TextType.BOLD)
        self.assertEqual(output, expected)

    def test_code(self):
        new_node = TextNode("This is text with a `code snippet` in the middle",TextType.TEXT)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code snippet", TextType.CODE),
            TextNode(" in the middle", TextType.TEXT),
            ]
        output = split_nodes_delimiter([new_node],"`", TextType.CODE)
        self.assertEqual(output, expected)