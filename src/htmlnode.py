class HTMLNode:
    def __init__(self, children=None, props=None, tag=None, value=None):
        self.props = props
        self.children = children
        self.tag = tag
        self.value = value

    def __repr__(self):
        return f"HTMLNode: {self.tag}, {self.value}"

    def to_html(self):
        raise NotImplementedError()

    def props_to_html_method(self):
        if self.props == None:
            raise Exception(f"{self} dont contain any props")
        attr_string = ""
        for key, value in self.props.items():
            attr_string += f' {key}="{value}"'
        return attr_string
