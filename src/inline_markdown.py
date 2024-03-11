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
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        words = re.split(r"!\[(.*?)\]\((.*?)\)", node.text)
        images = extract_markdown_images(node.text)
        for word in words:
            no_match = True
            if word == "":
                continue
            for image in images:
                if image[1] == word:
                    no_match = False
                    break
                if image[0] == word:
                    new_nodes.append(TextNode(image[0], text_type_image, image[1]))
                    no_match = False
                    break
            if no_match == True:
                new_nodes.append(TextNode(word, text_type_text, None))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        words = re.split(r"\[(.*?)\]\((.*?)\)", node.text)
        links = extract_markdown_links(node.text)
        for word in words:
            no_match = True
            if word == "":
                continue
            for link in links:
                if link[1] == word:
                    no_match = False
                    break
                if link[0] == word:
                    new_nodes.append(TextNode(link[0], text_type_link, link[1]))
                    no_match = False
                    break
            if no_match == True:
                new_nodes.append(TextNode(word, text_type_text, None))
    return new_nodes
