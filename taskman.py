from asyncio import Task
import os
def add_task(tasks, description, due_date): 
    tasks.append({"description": description, "due_date": due_date})

def view_task(tasks):
    if not tasks:
        print("No tasks found. ")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx + 1}. {task['description']} (Due: {task['due_date']})")

def remove_task(tasks, task_number):
    if 1 <= task_number <= len(tasks):
        del tasks[task_number - 1]
        print("task deleted")
    else:
        print("Invalid task number")
    
    def save_tasks(tasks, file_path):
        with open(file_path, "w") as f:
            for task in tasks:
                f.write(f"{task['description']} [{task['due_date']}]\n")

def load_tasks_from_file(file_path):
    tasks=[]
    if os.path.exists(file_path):
        with one(file_path, "r") as f:
            for line in f:
                descriprion,due_date = line.strip().split('|')
                tasks.append({"description": description, "due_date": due_date})
    return tasks

def main():
    task = []
    file_path = "tasks.txt"
    tasks = load_tasks_from_file(file_path)
    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Enter choice: (1/2/3/4) ")
        if choice == "1":
            description = input("Enter task description: ")
            due_task = input("Enter due date: ")
            add_task(tasks, description, due_task)
            save_tasks(tasks, file_path)    
        elif choice == "2":
            view_task(tasks)
        elif choice == "3":
            view_task(tasks)
            task_index = int((input|("Enter task index to delete: ")))
            delete_task(tasks, task_index)
            save_tasks(tasks, file_path)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()





