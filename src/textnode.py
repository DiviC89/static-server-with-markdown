from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, target) -> bool:
        return (
            self.text == target.text
            and self.text_type == target.text_type
            and self.url == target.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    tag = None
    value = text_node.text
    props = None
    if text_node.text_type == text_type_text:
        tag = None
    elif text_node.text_type == text_type_bold:
        tag = "b"
    elif text_node.text_type == text_type_italic:
        tag = "i"
    elif text_node.text_type == text_type_code:
        tag = "code"
    elif text_node.text_type == text_type_link:
        tag = "a"
        props = {"href": text_node.url}
    elif text_node.text_type == text_type_image:
        tag = "img"
        value = ""
        props = {"src": text_node.url, "alt": text_node.text}
    else:
        raise Exception("No valid tag found to covert textnode to LeafNode")
    new_leaf = LeafNode(tag, value, props)
    return new_leaf
