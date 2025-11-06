import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_eq_None_Link(self):
        node = TextNode("This is text", TextType.CODE_TEXT, None)
        node2 = TextNode("This is text", TextType.CODE_TEXT)
        self.assertEqual(node, node2)

    def test_eq_diff_text(self):
        node = TextNode("Some text", TextType.IMAGES, "./funnycat.png")
        node2 = TextNode("Some other text", TextType.IMAGES, "./funnycat.png")
        self.assertNotEqual(node, node2)

    def test_eq_diff_type(self):
        node = TextNode("Some text", TextType.LINKS, "./funnycat.png")
        node2 = TextNode("Some text", TextType.IMAGES, "./funnycat.png")
        self.assertNotEqual(node, node2)

    def test_eq_diff_url(self):
        node = TextNode("Some text", TextType.LINKS, "./funnycat.png")
        node2 = TextNode("Some text", TextType.LINKS, "./funnydog.png")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()