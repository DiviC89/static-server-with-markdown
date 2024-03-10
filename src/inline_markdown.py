import re

from textnode import TextNode, text_type_image, text_type_link, text_type_text


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
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    print(old_nodes)
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        split_by_delimiter = node.text.split(r"!\[(.*?)\]\((.*?)\)")
        if len(split_by_delimiter) % 2 == 0:
            raise Exception(
                f"This isn't valid markdown: {node.text}. \nMissing image tag in markdown text"
            )
        for i in range(0, len(split_by_delimiter)):
            if split_by_delimiter[i] == "":
                continue
            if i == 0 or i % 2 == 0:
                images = extract_markdown_images(split_by_delimiter[i])
                if len(images) == 0:
                    continue
                for img in images:
                    new_nodes.append(TextNode(img[0], text_type_image, img[1]))
            else:
                new_nodes.append(TextNode(split_by_delimiter[i], text_type_text))
    print(new_nodes)
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    return new_nodes
