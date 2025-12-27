class Tasker:
    tasks = []

    @classmethod
    def add_tasks(cls, num_items):
        for token in range(1, num_items + 1):
            item = input(f"{token}. Enter a task: ")
            cls.tasks.append(item)

    @classmethod
    def show_item(cls, index):
        if 0 <= index < len(cls.tasks):
            print(cls.tasks[index])
        else:
            print(f"Error: Index {index} is out of range.")

    @classmethod
    def remove_item(cls, index):
        if 0 <= index < len(cls.tasks):
            removed = cls.tasks.pop(index)
            print(f"Removed item: '{removed}'")
        else:
            print(f"Error: Index {index} is out of range. No item removed.")

    @classmethod
    def show_all(cls):
        if not cls.tasks:
            print("The task list is currently empty.")
        else:
            print("Current Tasks:")
            for idx, item in enumerate(cls.tasks, 1):
                print(f"{idx}. {item}")

    @classmethod
    def clear(cls):
        cls.tasks = []
