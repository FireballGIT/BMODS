# ===============================
# fileutil.py
# BAG Studios — File Utilities
# ===============================

import os
import shutil
import zipfile


# ===============================
# FILE CREATION
# ===============================

def make(path, content=""):
    """
    Creates a file at `path`.
    Optionally writes content.
    """
    if os.path.exists(path):
        return "Error: File already exists."

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return True


# ===============================
# RENAME FILE
# ===============================

def rename(path, new_name):
    """
    Renames a file or folder.
    """
    if not os.path.exists(path):
        return "Error: Path does not exist."

    directory = os.path.dirname(path)
    new_path = os.path.join(directory, new_name)

    os.rename(path, new_path)
    return new_path


# ===============================
# RENAME EXTENSION
# ===============================

def rename_ext(path, new_ext):
    """
    Changes a file's extension.
    """
    if not os.path.isfile(path):
        return "Error: File does not exist."

    if not new_ext.startswith("."):
        new_ext = "." + new_ext

    base = os.path.splitext(path)[0]
    new_path = base + new_ext

    os.rename(path, new_path)
    return new_path


# ===============================
# MOVE FILE / FOLDER
# ===============================

def move(src, dst):
    """
    Moves a file or folder.
    """
    if not os.path.exists(src):
        return "Error: Source does not exist."

    shutil.move(src, dst)
    return True


# ===============================
# COMPRESS FOLDER
# ===============================

def compress(folder_path, output_zip):
    """
    Compresses a folder into a ZIP file.
    """
    if not os.path.isdir(folder_path):
        return "Error: Folder does not exist."

    if not output_zip.endswith(".zip"):
        output_zip += ".zip"

    shutil.make_archive(
        base_name=output_zip.replace(".zip", ""),
        format="zip",
        root_dir=folder_path
    )

    return output_zip


# ===============================
# EXTRACT ZIP FILE
# ===============================

def extract(zip_path, output_dir):
    """
    Extracts a ZIP file.
    """
    if not zipfile.is_zipfile(zip_path):
        return "Error: Not a valid ZIP file."

    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(output_dir)

    return True
