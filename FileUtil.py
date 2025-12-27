import os
import shutil
import zipfile

class FileUtil:

    @staticmethod
    def make(path, content=""):
        if os.path.exists(path):
            return "Error: File already exists."
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return True

    @staticmethod
    def rename(path, new_name):
        if not os.path.exists(path):
            return "Error: Path does not exist."
        directory = os.path.dirname(path)
        new_path = os.path.join(directory, new_name)
        os.rename(path, new_path)
        return new_path

    @staticmethod
    def rename_ext(path, new_ext):
        if not os.path.isfile(path):
            return "Error: File does not exist."
        if not new_ext.startswith("."):
            new_ext = "." + new_ext
        base = os.path.splitext(path)[0]
        new_path = base + new_ext
        os.rename(path, new_path)
        return new_path

    @staticmethod
    def move(src, dst):
        if not os.path.exists(src):
            return "Error: Source does not exist."
        shutil.move(src, dst)
        return True

    @staticmethod
    def compress(folder_path, output_zip):
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

    @staticmethod
    def extract(zip_path, output_dir):
        if not zipfile.is_zipfile(zip_path):
            return "Error: Not a valid ZIP file."
        with zipfile.ZipFile(zip_path, "r") as z:
            z.extractall(output_dir)
        return True
