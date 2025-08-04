#To-do list project
#Define a class to manage a to-do-list
class ToDolist:
    def __init__(self):
        self.tasks = []
    def add_task(self,task):
        self.tasks.append({"task": task, "done": False})
        print(f"Task '{task}' added successfully")  
    def remove_task(self,task):
        for t in self.tasks:
            if t["task"]==task:
                self.tasks.remove(t)
                print("Task removed succesfully:")
                return
        print("Task is not found")

    def display_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                status = "Done" if task["done"]  else "Not Done"
                print (f"{index}. {task['task']} - {status}")
        else:
            print("Tour To-Do list is Empty")

    def mark_complete(self,task):
        task_index=int(input("Enter the task number to mark as done :")) - 1
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index] ["done"]= True
            print("Task marked as done!")
        else:
            print("Invalid task number")

def main():
    todo_list = ToDolist()
    while True:
        print("\nChoose an option:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Dispaly Tasks")
        print("4. Mark Task as Completed")
        print("5. Exit")
        
        choice = input("Enter your choice:")
        if choice == "1":
            task= input("Enter the task to add:")
            todo_list.add_task(task)
        elif choice == "2":
            task = input(" Enter the task to remove:")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            todo_list.mark_complete(None)
        elif choice == "5":
            print("Existing app")
            break    
        else:
            print("Invalid choice. Please enter a valid option")
main()            