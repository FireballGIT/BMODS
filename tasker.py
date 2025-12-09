#(C)2025 BMODS by BAG Studios. Licensed under the MIT License.

tasks = []

def add_tasks(num_items):
  for token in range(1, num_items + 1):
    item = input(f"{token}. Enter a task: ")
    tasks.append(item)

def show_item(index):
  # Use len() to prevent IndexError if index is out of range
  if 0 <= index < len(tasks):
    print(tasks[index])
  else:
    print(f"Error: Index {index} is out of range.")

def remove_item(index):
  if 0 <= index < len(tasks):
    removed = tasks.pop(index)
    print(f"Removed item: '{removed}'")
  else:
    print(f"Error: Index {index} is out of range. No item removed.")

def show_all():
  if not tasks:
    print("The task list is currently empty.")
  else:
    print("Current Tasks:")
    # Loop directly over the items for simpler access
    for index, item in enumerate(tasks, 1):
      print(f"{index}. {item}")
