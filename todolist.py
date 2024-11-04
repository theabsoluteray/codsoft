# Using tkinter for gui
import tkinter as tk
from tkinter import messagebox

# Using json for storing data 
import json

# and datetime for due date validation
from datetime import datetime


 
class Task:
    def __init__(self, title, due_date=None, priority="Low", status="Pending"):
        self.title = title
        self.due_date = due_date
        self.priority = priority
        self.status = status
    # converting to dictionary to store it in json
    def to_dict(self):
        return vars(self)

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.configure(bg="black")
        
        self.tasks = []
        self.filename = "tasks.json"
        self.load_tasks()

        # Title Entry
        tk.Label(root, text="Task Title:").grid(row=0, column=0, padx=10, pady=5)
        self.title_entry = tk.Entry(root, width=30)
        self.title_entry.grid(row=0, column=1, padx=10, pady=5)

        # Due Date Entry
        tk.Label(root, text="Due Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5)
        self.due_date_entry = tk.Entry(root, width=30)
        self.due_date_entry.grid(row=1, column=1, padx=10, pady=5)

        # Priority Dropdown
        tk.Label(root, text="Priority:").grid(row=2, column=0, padx=10, pady=5)
        self.priority_var = tk.StringVar(value="Low")
        self.priority_menu = tk.OptionMenu(root, self.priority_var, "Low", "Medium", "High")
        self.priority_menu.grid(row=2, column=1, padx=10, pady=5)

        # Task Button
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Task Listbox
        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
        self.update_task_listbox()

        # Delete Task Button
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=5, column=0, columnspan=2, pady=10)

    def add_task(self):
        title = self.title_entry.get()
        due_date = self.due_date_entry.get()
        priority = self.priority_var.get()

        if not title:
            messagebox.showwarning("Input Error", "Task title cannot be empty.")
            return
        
        try:
            if due_date:
                datetime.strptime(due_date, "%Y-%m-%d")  # Validate date format
        except ValueError:
            messagebox.showwarning("Date Error", "Due date must be in YYYY-MM-DD format.")
            return

        new_task = Task(title, due_date, priority)
        self.tasks.append(new_task)
        self.save_tasks()
        self.update_task_listbox()
        
        # Clear inputs
        self.title_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)
        self.priority_var.set("Low")
    
     # functions for deleting , updating , adding and loading tasks
    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.save_tasks()
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = f"{task.title} - Due: {task.due_date or 'N/A'}, Priority: {task.priority}, Status: {task.status}"
            self.task_listbox.insert(tk.END, display_text)

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=2)

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.tasks = [Task(**task) for task in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

if __name__ == "__main__":
    ray = tk.Tk()
    app = TodoListApp(ray)
    ray.mainloop()
