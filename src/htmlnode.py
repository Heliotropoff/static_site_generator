class HTMLnode:
    def __init__(self, tag = None, value = None, childern = None, props = None):
        self.tag = tag
        self.value = value
        self.children = childern
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