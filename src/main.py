import os
import shutil


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


def main() -> None:
    copy_folder(src="static", dst="public")


if __name__ == "__main__":
    main()
