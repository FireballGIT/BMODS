# Initialize a global list to store console messages
console = []
# Initialize a global flag to manage the state
consoleExists = False

def new(object_type):
    global console, consoleExists
    if object_type == "console":
        console = [] # Reset the console list
        consoleExists = True
        print("Console object created/reset.")
    elif object_type == "log":
        # Add this sometime else
        print("Log object type not yet implemented.")
    else:
        print("ERROR! Invalid object type.")

def log(msg):
    global console
    if consoleExists: # Check the boolean value directly
        console.append(msg)
        print(f"Logged: '{msg}'")
    else:
        print("ERROR! No existing console object.")

def terminate(index):
    global console
    if consoleExists:
        try:
            removed_item = console.pop(index)
            print(f"Terminated line {index}: '{removed_item}'")
        except IndexError:
            print(f"ERROR! Index {index} is out of range.")
    else:
        print("ERROR! No existing console object.")

def clear():
    global console
    if consoleExists:
        console = []
        print("Console cleared.")
    else:
        print("ERROR! No existing console object.")

def println(index):
    """Prints a single line from the console at the specified index."""
    if consoleExists:
        try:
            print(console[index])
        except IndexError:
            print(f"ERROR! Index {index} is out of range.")
    else:
        print("ERROR! No existing console object.")


def prntall():
    """Prints all items currently in the console."""
    if consoleExists:
        if not console:
            print("Console is empty.")
            return
            
        print("--- Console Start ---")
        for index, item in enumerate(console):
            print(f"[{index}]: {item}")
        print("--- Console End ---")
    else:
        print("ERROR! No existing console object.")
