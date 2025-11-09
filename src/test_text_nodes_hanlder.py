import unittest
from textnode import TextNode, TextType
from text_nodes_handler import split_nodes_delimiter,split_nodes_image,split_nodes_link

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

    def test_split_images(self):
        node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                ],
                new_nodes,
                )
    def test_split_links(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT,)
        new_nodes = split_nodes_link([node])
        test_outcome = [ TextNode("This is text with a link ", TextType.TEXT),
                        TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                        TextNode(" and ", TextType.TEXT),
                        TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),]
        self.assertEqual(
            new_nodes, test_outcome
        )
