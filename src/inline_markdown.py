import re

from textnode import TextNode, text_type_text

pattern = re.pattern(r"!\[(.*?)\]\((.*?)\)")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        split_by_delimiter = node.text.split(delimiter)
        if len(split_by_delimiter) % 2 == 0:
            raise Exception(
                f"This isn't valid markdown: {node.text}. \nMissing opening or closing tag for {text_type} with delimiter {delimiter}"
            )
        for i in range(0, len(split_by_delimiter)):
            if split_by_delimiter[i] == "":
                continue
            if i == 0 or i % 2 == 0:
                new_nodes.append(TextNode(split_by_delimiter[i], text_type_text))
            else:
                new_nodes.append(TextNode(split_by_delimiter[i], text_type))
    return new_nodes

def extract_markdown_images(text):
    


def extract_markdown_links(text):
