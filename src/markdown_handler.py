from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise ValueError(f"Unmatched delimiter {delimiter}")
            for i in enumerate(parts):
                if parts[i] == "":
                    continue
            if i % 2 == 0:
                new_node = TextNode(parts[i], TextType.TEXT)
                new_nodes.append(new_node)
            elif i % 2 !=0:
                new_node = TextNode(parts[i], text_type)
                new_nodes.append(new_node)
