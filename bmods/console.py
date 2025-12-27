import datetime
from pathlib import Path

class Console:
    console = []
    consoleExists = False

    @staticmethod
    def get_timestamp():
        return datetime.datetime.now().strftime("%m/%d/%Y %H:%M")

    @classmethod
    def new(cls, object_type):
        if object_type == "console":
            cls.console = []
            cls.consoleExists = True
            print(f"[{cls.get_timestamp()}] Console object created/reset.")
        elif object_type == "log":
            print(f"[{cls.get_timestamp()}] Log object type not yet implemented.")
        else:
            print(f"[{cls.get_timestamp()}] ERROR! Invalid object type.")

    @classmethod
    def log(cls, msg):
        if cls.consoleExists:
            timestamped_msg = f"[{cls.get_timestamp()}] {msg}"
            cls.console.append(timestamped_msg)
            print(f"Logged: '{timestamped_msg}'")
        else:
            print(f"[{cls.get_timestamp()}] ERROR! No existing console object.")

    @classmethod
    def terminate(cls, index):
        if cls.consoleExists:
            try:
                removed_item = cls.console.pop(index)
                cls.log(f"Terminated line {index}: '{removed_item.strip()}'")
            except IndexError:
                cls.log(f"ERROR! Index {index} is out of range.")
        else:
            print(f"[{cls.get_timestamp()}] ERROR! No existing console object.")

    @classmethod
    def clear(cls):
        if cls.consoleExists:
            cls.console = []
            cls.log("Console cleared.")
        else:
            print(f"[{cls.get_timestamp()}] ERROR! No existing console object.")

    @classmethod
    def println(cls, index):
        if cls.consoleExists:
            try:
                print(cls.console[index])
            except IndexError:
                print(f"[{cls.get_timestamp()}] ERROR! Index {index} is out of range.")
        else:
            print(f"[{cls.get_timestamp()}] ERROR! No existing console object.")

    @classmethod
    def prntall(cls):
        if cls.consoleExists:
            if not cls.console:
                cls.log("Console is empty.")
                return
            print("--- Console Start ---")
            for item in cls.console:
                print(item)
            print("--- Console End ---")
        else:
            print(f"[{cls.get_timestamp()}] ERROR! No existing console object.")

    @classmethod
    def export_log(cls, filename="output_log", directory="."):
        if cls.consoleExists and cls.console:
            try:
                file_path = Path(directory) / f"{filename}.bmlog"
                file_path.parent.mkdir(parents=True, exist_ok=True)
                with open(file_path, "w") as f:
                    for line in cls.console:
                        f.write(f"{line}\n")
                cls.log(f"Successfully exported console to '{file_path}'.")
            except IOError as e:
                cls.log(f"ERROR! Could not write to file {file_path}: {e}")
        elif cls.consoleExists and not cls.console:
            cls.log("Console is empty; nothing to export.")
        else:
            cls.log("ERROR! No existing console object to export.")
