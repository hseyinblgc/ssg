import os
import shutil
import sys
from pathlib import Path

from blocks import markdown_to_html_node


def copy_folder(src: str, dst: str) -> None:
    work_dir: str = os.getcwd()
    src_dir: str = os.path.normpath(os.path.join(work_dir, src))
    dest_dir: str = os.path.normpath(os.path.join(work_dir, dst))

    try:
        items: list[str] = os.listdir(src_dir)
        if len(items) == 0:
            return
    except FileNotFoundError:
        return

    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)

    for item in items:
        src_file: str = os.path.join(src_dir, item)
        dest_file: str = os.path.join(dest_dir, item)
        if os.path.isfile(path=src_file):
            print(f"{shutil.copy(src_file, dest_file)}")
        elif os.path.isdir(src_file):
            copy_folder(src_file, dest_file)


def extract_title(markdown: str) -> str:
    lines: list[str] = list(
        filter(lambda line: line.startswith("# "), markdown.split("\n"))
    )

    if len(lines) == 0:
        raise ValueError(f"Invalid format: {markdown}")
    return lines[0].lstrip("# ")


def generate_page(from_path, template_path, dest_path, basepath) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    os.makedirs(name=os.path.dirname(dest_path), exist_ok=True)

    with open(file=from_path, mode="r") as sf:
        markdown: str = sf.read()

    with open(file=template_path, mode="r") as tf:
        temp: str = tf.read()

    content: str = markdown_to_html_node(markdown).to_html()
    title: str = extract_title(markdown)
    temp = temp.replace("{{ Title }}", title).replace("{{ Content }}", content)
    temp = temp.replace('href="/', f'href="{basepath}').replace(
        'src="/', f'src="{basepath}'
    )

    with open(file=dest_path, mode="w") as df:
        df.write(temp)


def generate_pages_recursive(
    dir_path_content, template_path, dest_dir_path, basepath
) -> None:

    src: Path = Path(dir_path_content)
    dest: Path = Path(dest_dir_path)

    for item in src.rglob("*.md"):
        generate_page(
            item,
            template_path,
            dest
            / item.relative_to(src).with_suffix(
                ".html",
            ),
            basepath,
        )


def main() -> None:
    basepath: str = sys.argv[1] if len(sys.argv) > 1 else "/"
    copy_folder(src="static", dst="docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)


if __name__ == "__main__":
    main()
