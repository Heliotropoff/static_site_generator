from text_nodes_handler import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType
from htmlnode import ParentNode, LeafNode
from pprint import pprint
from enum import Enum
import re

def markdown_to_blocks(markdown):
    elements = markdown.split("\n\n")
    blocks = []
    for element in elements:
        element = element.strip()
        if element:
            blocks.append(element)
    return blocks

# md = """# This is a heading

# This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

# - This is the first list item in a list block
# - This is a list item
# - This is another list item
# """
# tt = markdown_to_blocks(md)
# pprint(tt)

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


def block_to_block_type(md_block):
    block_patterns = {
        r"#{1,6} .+": BlockType.HEADING,
        r"```([\s\S]+?)```":BlockType.CODE,
        r">(.+)":BlockType.QUOTE,
        r"- (.+)":BlockType.UNORDERED_LIST,
        r"\d+\. .+":BlockType.ORDERED_LIST
        }
    block_type = ""
    for pattern in block_patterns:
        pattern_match = re.search(pattern=pattern, string=md_block)
        if pattern_match:
            block_type = block_patterns[pattern]
    if not block_type:
        block_type = BlockType.PARAGRAPH

    return block_type

def markdown_to_html_node(md_document):
    root_children = []
    md_blocks = markdown_to_blocks(md_document)
    for md_block in md_blocks:
        block_type = block_to_block_type(md_block=md_block)
        if block_type != BlockType.CODE:
            block_HTML_node = block_to_html_node(block=md_block,block_type=block_type)
            root_children.append(block_HTML_node)
        else:
            stripped_code = md_block.strip("```").lstrip("\n")
            code_text_node = TextNode(text=stripped_code, text_type=TextType.CODE)
            code_HTML_node = text_node_to_html_node(code_text_node)
            code_block_node = ParentNode(tag="pre", children=[code_HTML_node])
            root_children.append(code_block_node)

    return ParentNode(tag="div", children=root_children)

def text_to_children(text):
    children_html_nodes = []
    children_text_nodes = text_to_textnodes(text)
    for child_node in children_text_nodes:
        new_child = text_node_to_html_node(child_node)
        children_html_nodes.append(new_child)
    return children_html_nodes

def list_items_to_children(text, block_list_type):
    list_elements = text.split("\n")
    list_items = []
    for element in list_elements:
        if element != "":
            if block_list_type == BlockType.UNORDERED_LIST:
                preformatted_element = re.sub(r"^\s*[-*]\s+", "", element)
            elif block_list_type == BlockType.ORDERED_LIST:
                preformatted_element = re.sub(r"^\d+\.\s*", "", element)
            else:
                raise ValueError(f"Type Mismatch: {block_list_type.name} was passed for processing list items")
            stripped_element = preformatted_element.strip()
            formatted_elements = text_to_textnodes(stripped_element)
            li_parts = []
            for formatted_element in formatted_elements:
                processed_element = text_node_to_html_node(formatted_element)
                li_parts.append(processed_element)
            new_item = ParentNode("li", children=li_parts)
            list_items.append(new_item)
    return list_items

def get_correct_header_tag(heading_text):
    header_pattern = r"^(#+)"
    header_size = len(re.match(header_pattern, heading_text).group(0))
    match header_size:
        case 1:
            return "h1"
        case 2:
            return "h2"
        case 3:
            return "h3"
        case 4:
            return "h4"
        case 5:
            return "h5"
        case 6:
            return "h6"
        case _:
            raise ValueError("Wrong header size")



def block_to_html_node(block, block_type):
    if block_type == BlockType.PARAGRAPH:
        block = block.replace("\n", " ")
    if block_type != BlockType.UNORDERED_LIST and block_type != BlockType.ORDERED_LIST:
        children = text_to_children(block)
    else:
        children = list_items_to_children(text=block, block_list_type=block_type)
    match block_type:
        case BlockType.PARAGRAPH:
            return ParentNode(tag="p",children=children)
        case BlockType.HEADING:
            preformatted_header = re.sub(r"^(#+)", "", block)
            h_tag = get_correct_header_tag(preformatted_header)
            return ParentNode(tag=h_tag, children=children)
        case BlockType.QUOTE:
            return ParentNode(tag="blockquote", children=children)
        case BlockType.UNORDERED_LIST:
            return ParentNode(tag="ul", children=children)
        case BlockType.ORDERED_LIST:
            return ParentNode(tag="ol", children=children)
        case _:
            raise Exception("Code block or Unknown block type")


md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""


# md = """
# This is **bolded** paragraph
# text in a p
# tag here

# This is another paragraph with _italic_ text and `code` here

# """
# md = """
# ```
# This is text that _should_ remain
# the **same** even with inline stuff
# ```
# """

# ms = "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>"
# ls = """
# - milk
# - juice
# - cat food
# """
# ls2 = """
# 1. milk
# 2. juice
# 3. cat food
# """
# testo = markdown_to_html_node(ls2)
# pprint(testo.to_html())
# pprint(ms)

# print(ms == testo)