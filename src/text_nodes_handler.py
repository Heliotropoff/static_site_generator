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
            processed_string = node.text
            while processed_string:
                extracted_data = extract_markdown_images(processed_string)
                if extracted_data:
                    processed_img_item = extracted_data[0]
                    alt_text = processed_img_item[0]
                    img_url = processed_img_item[1]
                    new_img_node = TextNode(alt_text, TextType.IMAGE, img_url)
                    sections = processed_string.split(f"![{alt_text}]({img_url})", 1)
                    preceding_section = sections[0]
                    following_section = sections[1]
                    if preceding_section:
                        new_plain_text = TextNode(preceding_section, TextType.TEXT)
                        new_nodes.append(new_plain_text)
                    new_nodes.append(new_img_node)
                    processed_string = following_section
                    if processed_string == "":
                        break
                else:
                    break
            if processed_string:
                new_plain_text = TextNode(processed_string, TextType.TEXT)
                new_nodes.append(new_plain_text)
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            processed_string = node.text
            while processed_string:
                extracted_data = extract_markdown_links(processed_string)
                if extracted_data:
                    processed_link_item = extracted_data[0]
                    anchor_text = processed_link_item[0]
                    link_url = processed_link_item[1]
                    new_link_node = TextNode(anchor_text, TextType.LINK, link_url)
                    sections = processed_string.split(f"[{anchor_text}]({link_url})", 1)
                    preceding_section = sections[0]
                    following_section = sections[1]
                    if preceding_section:
                        new_plain_text = TextNode(preceding_section, TextType.TEXT)
                        new_nodes.append(new_plain_text)
                    new_nodes.append(new_link_node)
                    processed_string = following_section
                    if processed_string == "":
                        break
                else:
                    break
            if processed_string:
                new_plain_text = TextNode(processed_string, TextType.TEXT)
                new_nodes.append(new_plain_text)
    return new_nodes
