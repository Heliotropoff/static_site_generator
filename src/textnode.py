from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):

    PLAIN_TEXT = "text (plain)"
    BOLD_TEXT = "**Bold text**"
    ITALIC_TEXT = "_Italic text_"
    CODE_TEXT = "`Code text`"
    LINKS = "[anchor text](url)"
    IMAGES = "![alt text](url)"

class TextNode():

    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url


    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.PLAIN_TEXT:
            return LeafNode(tag = None, value = text_node.text)
        case TextType.BOLD_TEXT:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC_TEXT:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE_TEXT:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINKS:
            return LeafNode(tag="a", value=text_node.text, props={"href":text_node.url})
        case TextType.IMAGES:
            return LeafNode(tag="img", value="", props={"src":text_node.url, "alt":text_node.text})
        case _:
            raise Exception("Unknown text node type")