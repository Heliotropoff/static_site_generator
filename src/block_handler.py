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