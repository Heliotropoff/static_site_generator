import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_None_Link(self):
        node = TextNode("This is text", TextType.CODE, None)
        node2 = TextNode("This is text", TextType.CODE)
        self.assertEqual(node, node2)

    def test_eq_diff_text(self):
        node = TextNode("Some text", TextType.IMAGE, "./funnycat.png")
        node2 = TextNode("Some other text", TextType.IMAGE, "./funnycat.png")
        self.assertNotEqual(node, node2)

    def test_eq_diff_type(self):
        node = TextNode("Some text", TextType.LINK, "./funnycat.png")
        node2 = TextNode("Some text", TextType.IMAGE, "./funnycat.png")
        self.assertNotEqual(node, node2)

    def test_eq_diff_url(self):
        node = TextNode("Some text", TextType.LINK, "./funnycat.png")
        node2 = TextNode("Some text", TextType.LINK, "./funnydog.png")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()