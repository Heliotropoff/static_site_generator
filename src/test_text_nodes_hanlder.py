import unittest
from textnode import TextNode, TextType
from text_nodes_handler import split_nodes_delimiter,split_nodes_image,split_nodes_link,text_to_textnodes

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
        anticipate = [ TextNode("This is text with a link ", TextType.TEXT),
                        TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                        TextNode(" and ", TextType.TEXT),
                        TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),]
        self.assertEqual(
            new_nodes, anticipate
        )

    def test_text_to_nodes1(self):
        original_text = "This is just a plain text, maaan"
        anticipate = [TextNode(original_text, TextType.TEXT)]
        result = text_to_textnodes(original_text)
        self.assertEqual(result, anticipate)

    def test_text_to_nodes2(self):
        original_text = "Now this one is _interesting_ it has some images! Like this one ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        anticipate = [
            TextNode("Now this one is ", TextType.TEXT),
            TextNode("interesting", TextType.ITALIC),
            TextNode(" it has some images! Like this one ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link",TextType.LINK,"https://boot.dev")
            ]
        result = text_to_textnodes(original_text)
        self.assertEqual(result, anticipate)

    def test_text_to_nodes3(self):
        original_text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        anticipate = [TextNode("This is ", TextType.TEXT),
                      TextNode("text", TextType.BOLD),
                      TextNode(" with an ",TextType.TEXT),
                      TextNode("italic", TextType.ITALIC),
                      TextNode(" word and a ", TextType.TEXT),
                      TextNode("code block", TextType.CODE),
                      TextNode(" and an ", TextType.TEXT),
                      TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                      TextNode(" and a ", TextType.TEXT),
                      TextNode("link", TextType.LINK,"https://boot.dev")]
        result = text_to_textnodes(original_text)
        self.assertEqual(result, anticipate)