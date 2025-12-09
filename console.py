import datetime # Import the datetime module
import os # Import the OS module for directory handling
from pathlib import Path # Use pathlib for robust path joining

# Initialize a global list to store console messages (now with timestamps)
console = []
consoleExists = False

def get_timestamp():
    """Generates the current time in the required M/D/Y H:M format."""
    # Use strftime to format the current datetime object
    return datetime.datetime.now().strftime("%m/%d/%Y %H:%M")

def new(object_type):
    """Initializes or resets the console based on the object_type."""
    global console, consoleExists
    if object_type == "console":
        console = []
        consoleExists = True
        print(f"[{get_timestamp()}] Console object created/reset.")
    elif object_type == "log":
        print(f"[{get_timestamp()}] Log object type not yet implemented.")
    else:
        print(f"[{get_timestamp()}] ERROR! Invalid object type.")

def log(msg):
    """Appends a message with a timestamp to the console if it exists."""
    global console
    if consoleExists:
        timestamped_msg = f"[{get_timestamp()}] {msg}"
        console.append(timestamped_msg)
        print(f"Logged: '{timestamped_msg}'")
    else:
        print(f"[{get_timestamp()}] ERROR! No existing console object.")

def terminate(index):
    """Removes an item at the specified index from the console."""
    global console
    if consoleExists:
        try:
            removed_item = console.pop(index)
            log(f"Terminated line {index}: '{removed_item.strip()}'") # Log the termination event
        except IndexError:
            log(f"ERROR! Index {index} is out of range.")
    else:
        print(f"[{get_timestamp()}] ERROR! No existing console object.")

def clear():
    """Clears all entries from the console."""
    global console
    if consoleExists:
        console = []
        log("Console cleared.")
    else:
        print(f"[{get_timestamp()}] ERROR! No existing console object.")

def println(index):
    """Prints a single line from the console at the specified index."""
    if consoleExists:
        try:
            print(console[index])
        except IndexError:
            print(f"[{get_timestamp()}] ERROR! Index {index} is out of range.")
    else:
        print(f"[{get_timestamp()}] ERROR! No existing console object.")

def prntall():
    """Prints all items currently in the console."""
    if consoleExists:
        if not console:
            log("Console is empty.")
            return

        print("--- Console Start ---")
        for index, item in enumerate(console):
            print(item) # Items already have timestamps
        print("--- Console End ---")
    else:
        print(f"[{get_timestamp()}] ERROR! No existing console object.")

def export_log(filename="output_log", directory="."):
    """
    Exports the current console contents to a .bmlog file in a specified directory.
    Uses pathlib for cross-platform path handling.
    """
    global console
    if consoleExists and console:
        try:
            # Create the full file path using pathlib for robust handling
            file_path = Path(directory) / f"{filename}.bmlog"
            
            # Ensure the target directory exists
            file_path.parent.mkdir(parents=True, exist_ok=True) 

            with open(file_path, 'w') as f:
                for line in console:
                    f.write(f"{line}\n")
            log(f"Successfully exported console to '{file_path}'.")
        except IOError as e:
            log(f"ERROR! Could not write to file {file_path}: {e}")
    elif consoleExists and not console:
        log("Console is empty; nothing to export.")
    else:
        log("ERROR! No existing console object to export.")
