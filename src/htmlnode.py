class HTMLnode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        if self.props == "" or self.props == None:
            return ""
        result = ""
        for tag, value in self.props.items():
            result += f" {tag}=\"{value}\""
        return result
    def __repr__(self):
        return f"HTMLnode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLnode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        opening_tag = f"<{self.tag}>"
        closing_tag = f"</{self.tag}>"
        element = opening_tag + self.value + closing_tag
        return element

class ParentNode(HTMLnode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag=tag,children=children,props=props)
    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag provided")
        if self.children is None:
            raise ValueError("Children elemetns are missing!")

        opening_tag = f"<{self.tag}>"
        closing_tag = f"</{self.tag}>"
        element = opening_tag
        for child in self.children:
            element += child.to_html()
        element += closing_tag
        return element
