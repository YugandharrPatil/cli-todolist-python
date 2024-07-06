import argparse  # for passing command line arguments
import os  # file operations of current machine

# GLOBAL CONSTANTS
FILE_NAME = "tasks.txt"


def create_parser():
    parser = argparse.ArgumentParser(description="CLI Todo List App")
    parser.add_argument("-a", "--add", metavar="", help="Add a new task")
    parser.add_argument("-l", "--list", action="store_true", help="List all tasks")
    parser.add_argument("-r", "--remove", metavar="", help="Remove a task by index")
    return parser


def add_task(task):
    with open(FILE_NAME, "a") as file:
        file.write(task + "\n")


def list_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")
    else:
        print("No tasks found.")


def remove_task(index):
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()
        with open(FILE_NAME, "w") as file:
            for i, task in enumerate(tasks, start=1):
                # write all tasks back to the file except the one with the passed in index, thereby deleting it
                if i != index:
                    file.write(task)
        print("Task removed successfully.")
    else:
        print("No tasks found.")


def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        list_tasks()
    elif args.remove:
        remove_task(int(args.remove))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
