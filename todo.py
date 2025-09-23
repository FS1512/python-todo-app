import os

FILE_NAME = "todo.txt"

def load():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                tasks.append(line.strip())
    return tasks

def save(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")
            
def view(tasks):
    if not tasks:
        print("\nTo Do list empty!!")
    else:
        print("\n--- To Do ---")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        print("----------------------")
        
def add(tasks):
    new = input("Enter new task: ")
    if new:
        tasks.append(new)
        save(tasks)
        print(f"Task '{new}' added.")
    else:
        print("Task cannot be empty")
        
def remove(tasks):
    view(tasks)
    if not tasks:
        return 
    
    try: 
        task_number = int(input("Enter the number of the task to remove: "))
        if 1<= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            save(tasks)
            print(f"Task '{removed}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
        
if __name__ == "__main__":
    tasks = load()

    while True:
        print("\n--- To Do Menu ---\n1. View tasks\n2. Add task\n3. Remove task\n4. Exit")
        ch = input("Enter your choice: ")
        
        if ch == '1':
            view(tasks)
        elif ch == '2':
            add(tasks)
        elif ch == '3':
            remove(tasks)
        elif ch == '4':
            print("Exiting Application..")
            break
        else:
            print("Invalid Input. Please try again.")
