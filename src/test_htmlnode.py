import unittest
from htmlnode import HTMLnode

class TestHTMLnode(unittest.TestCase):
    def test_repr(self):
        node = HTMLnode("<h1>","Awesome title")
        obj = repr(node)
        self.assertEqual(obj, "HTMLnode(<h1>, Awesome title, None, None)")

    def test_props(self):
        node = HTMLnode("<h1>", "Hehe", props={"href":"https://www.google.com", "target":"_blank"})
        output = node.props_to_html()
        self.assertEqual(output, ' href="https://www.google.com" target="_blank"')

    def test_to_html_error(self):
        node = HTMLnode("<h1>", "Hehe", props={"href":"https://www.google.com", "target":"_blank"})
        with self.assertRaises(NotImplementedError):
            node.to_html()