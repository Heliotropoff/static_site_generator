from textnode import TextNode, TextType
from extract_links import extract_markdown_links, extract_markdown_images

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise ValueError(f"Unmatched delimiter {delimiter}")
            for i, part in enumerate(parts):
                if part == "":
                    continue
                if i % 2 == 0:
                    new_node = TextNode(part, TextType.TEXT)
                    new_nodes.append(new_node)
                elif i % 2 !=0:
                    new_node = TextNode(part, text_type)
                    new_nodes.append(new_node)
    return new_nodes

def split_nodes_image(olds_nodes):
    new_nodes = []
    for node in olds_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            extracted_img_data = extract_markdown_links(node.text)
            for img_item in extracted_img_data:
                alt_text = img_item[0]
                img_url = img_item[1]
                new_img_node = TextNode(alt_text, TextType.IMAGE, img_url)
                sections = node.text.split(f"![{alt_text}]({img_url})", 1)
                print(f"IMG_NODE: {new_img_node}")
                print(f"SECTION: {sections}")


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            extracted_link_data = extract_markdown_links(node.text)
            for link_item in extracted_link_data:
                anchor_text = link_item[0]
                anchor_text = link_item[1]
                new_lin_node = TextNode(anchor_text,TextType.LINK,link_url)
                sections = node.text.split(f"![{anchor_text}]({anchor_text})", 1)
                print(f"IMG_NODE: {new_lin_node}")
                print(f"SECTION: {sections}")
