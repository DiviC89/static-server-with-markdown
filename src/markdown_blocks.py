import re

block_type_heading = "heading"
block_type_paragraph = "paragraph"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"


def markdown_to_blocks(markdown):
    new_blocks = []
    lines = markdown.split("\n")
    new_block = ""
    for line in lines:
        if len(line) > 0:
            new_block += f"{line}\n"
        elif len(new_block) > 0:
            new_blocks.append(new_block.strip("\n "))
            new_block = ""
    return new_blocks


def block_to_block_type(markdown_block):
    is_paragraph = re.findall(
        r"^#+\s", markdown_block
    )  # find paragraph that starts with 1 - 6 # and a space.
    if len(is_paragraph) > 0:
        return block_type_heading
    if markdown_block.startswith("```") and markdown_block.endswith("```"):
        return block_type_code
    markdown_lines = markdown_block.split("\n")
    first_two_characters = ""
    for line in markdown_lines:
        first_two_characters += f"{line[0]}{line[1]}"
        # Get the two first characters to be able to find if every line starts with \d., *, - or >
    first_char = first_two_characters[::2]
    true_quote = False
    for char in first_char:
        true_quote = char == ">"
        if not true_quote:
            break
    if true_quote:
        return block_type_quote
    ulist = False
    for char in first_char:
        ulist = char == "*" or char == "-"
        if not ulist:
            break
    if ulist:
        return block_type_ulist
    olist = False
    # Get the 2nd char aswell for comparison to see if it's an ordered list.
    second_char = first_two_characters[1::2]
    for i in range(len(first_char)):
        olist = f"{i+1}" == first_char[i] and second_char[i] == "."
        # if not olist:
        #     break
    if olist:
        return block_type_olist
    return block_type_paragraph
