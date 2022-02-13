from pathlib import Path
from sys import argv
from shutil import move


def get_dir(filename):
    "Takes filename and returns the name of the parent directory."
    ext = filename.suffix[1:]
    return dirs.get(ext, "M")


dirs = {
    # Images
    "jpeg": "Images1",
    "png": "Images1",
    "jpg": "Images1",
    "gif": "Images1",

    # Videos
    "mp4": "Videos1",
    "mkv": "Videos1",
    "webm": "Videos1",
    "srt": "Videos1",

    # Music
    "mp3": "Music1",

    # Code
    "js": "Code1",
    "py": "Code1",
    "cpp": "Code1",
    "html": "Code1",
    "css": "Code1",
    "clj": "Code1",
    "sh": "Code1",

    # Docs
    "doc": "Docs1",
    "txt": "Docs1",
    "rtf": "Docs1",
    "docx": "Docs1",
    "pdf": "Docs1",
    "csv": "Docs1",
    "ppt": "Docs1",
    "pptx": "Docs1",
    "pages": "Docs1",
    "xlsx": "Docs1",

    # Books
    "epub": "Books1",
    "mobi": "Books1",

    # Stupid
    ".DS_Store": "Stupid1"

}


if len(argv) != 2:
    print("=" * 35)
    print("[ERROR] Invalud number of args")
    print("[Usage] python {Path(__file__).name} <dir_path>")
    print("=" * 35)
    exit(1)


# Directory Path
PATH = Path(argv[1])

for filename in PATH.iterdir():

    path_to_file = filename.absolute()

    if path_to_file.is_file():
        destination = PATH / get_dir(filename)

        if not destination.exists():
            destination.mkdir()

        move(str(path_to_file), str(destination))
