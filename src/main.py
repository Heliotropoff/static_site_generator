from textnode import TextNode, TextType
from htmlnode import HTMLnode
def main():
    new_text_node = TextNode("Some text here", TextType.ITALIC, "https://www.boot.dev")
    print(new_text_node)
    new_html_node = HTMLnode("<h1>","Awesome title")
    print(new_html_node)
    another_html_node = HTMLnode("<h1>", "Hehe", props={"href":"https://www.google.com", "target":"_blank"})
    t = another_html_node.props_to_html()
    print(t)


if __name__ == "__main__":
    main()
