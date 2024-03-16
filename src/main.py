import os
import shutil

from markdown_blocks import extract_title, markdown_to_html_node


def get_dir_content(path):
    return os.listdir(path)


def walk(current_path):
    tree = {}

    content = get_dir_content(current_path)
    if content == None or len(content) <= 0:
        return tree
    for item in content:
        if len(item.split(".")) > 1:
            tree[item] = item
        else:
            tree[item] = walk(f"{current_path}{item}/")
    return tree


def empty_out_folder(public_path):
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    return


def create_new_public(dictionary: dict, static_path, current_path):
    if not os.path.exists(current_path):
        os.mkdir(current_path)

    for key, value in dictionary.items():
        if isinstance(value, dict):
            create_new_public(value, f"{static_path}{key}/", f"{current_path}{key}/")
        else:
            shutil.copy(f"{static_path}/{value}", f"{current_path}{value}")
    return


def static_to_public(static_path, public_path):
    empty_out_folder(public_path)
    static_tree = walk(static_path)
    create_new_public(static_tree, static_path, public_path)
    return


def generate_page(from_path, template_path, dest_path):
    markdown_file = open(from_path)
    markdown = markdown_file.read()
    markdown_file.close()
    template_file = open(template_path)
    template = template_file.read()
    template_file.close()
    title = extract_title(markdown)
    content = markdown_to_html_node("\n".join(markdown.split("\n")[1:])).to_html()
    template_with_title = template.replace("{{ Title }}", title)
    new_page = template_with_title.replace("{{ Content }}", content)

    index_file = open(f"{dest_path}index.html", "w")
    index_file.write(new_page)
    index_file.close()


def generate_pages_recursive(current_path, destination_path, template_path):
    if not os.path.exists(destination_path):
        os.mkdir(destination_path)
    content = get_dir_content(current_path)
    for item in content:
        if len(item.split(".")) == 1:
            generate_pages_recursive(
                f"{current_path}{item}/", f"{destination_path}{item}/", template_path
            )
        else:
            generate_page(f"{current_path}{item}", template_path, destination_path)


def main():
    path = os.getcwd()
    static_to_public(f"{path}/static/", f"{path}/public/")
    generate_pages_recursive(
        f"{path}/content/", f"{path}/public/", f"{path}/template.html"
    )


main()
