import os
import shutil


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


def empty_out_folder():
    shutil.rmtree("../public")
    return


def create_new_public(dictionary: dict, current_path="../public/"):
    if not os.path.exists(current_path):
        os.mkdir(current_path)

    for key, value in dictionary.items():
        if isinstance(value, dict):
            create_new_public(value, f"{current_path}{key}/")
        else:
            static_path = current_path.replace("../public/", "../static/")
            print(static_path)
            shutil.copy(f"{static_path}{value}", f"{current_path}{value}")
    return


def static_to_public():
    empty_out_folder()
    static_tree = walk("../static/")
    create_new_public(static_tree)


def main():
    static_to_public()


main()
