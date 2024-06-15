import tkinter as tk
from tkinter import messagebox, simpledialog
import json
from datetime import datetime

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App with Deadlines and Priorities")
        self.root.configure(bg="lightblue")
        
        # List to store tasks
        self.tasks = []
        
        # Load tasks from file
        self.load_tasks()
        
        # UI Elements
        self.frame = tk.Frame(root, bg="lightblue")
        self.frame.pack(pady=10)
        
        self.task_entry = tk.Entry(self.frame, width=30)
        self.task_entry.grid(row=0, column=0, padx=5)
        
        self.add_task_button = tk.Button(self.frame, text="Add Task", command=self.add_task, bg="white")
        self.add_task_button.grid(row=0, column=1, padx=5)
        
        self.task_listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)
        
        self.update_task_button = tk.Button(root, text="Update Task", command=self.update_task, bg="white")
        self.update_task_button.pack(side=tk.LEFT, padx=5)
        
        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg="white")
        self.delete_task_button.pack(side=tk.RIGHT, padx=5)
        
        self.save_tasks_button = tk.Button(root, text="Save Tasks", command=self.save_tasks, bg="white")
        self.save_tasks_button.pack(pady=5)
        
        self.update_task_listbox()
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            deadline = simpledialog.askstring("Input", "Enter deadline (YYYY-MM-DD):")
            priority = simpledialog.askinteger("Input", "Enter priority (1-5):", minvalue=1, maxvalue=5)
            if deadline:
                try:
                    datetime.strptime(deadline, "%Y-%m-%d")
                except ValueError:
                    messagebox.showwarning("Warning", "Invalid date format. Use YYYY-MM-DD.")
                    return
            
            if priority:
                self.tasks.append({"task": task, "deadline": deadline, "priority": priority})
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a priority.")
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    
    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task = self.task_entry.get()
            if new_task:
                deadline = simpledialog.askstring("Input", "Enter deadline (YYYY-MM-DD):")
                priority = simpledialog.askinteger("Input", "Enter priority (1-5):", minvalue=1, maxvalue=5)
                if deadline:
                    try:
                        datetime.strptime(deadline, "%Y-%m-%d")
                    except ValueError:
                        messagebox.showwarning("Warning", "Invalid date format. Use YYYY-MM-DD.")
                        return
                
                if priority:
                    self.tasks[selected_task_index[0]] = {"task": new_task, "deadline": deadline, "priority": priority}
                    self.update_task_listbox()
                    self.task_entry.delete(0, tk.END)
                else:
                    messagebox.showwarning("Warning", "You must enter a priority.")
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        else:
            messagebox.showwarning("Warning", "You must select a task to update.")
    
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")
    
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_text = f"{task['task']} (Deadline: {task['deadline']}, Priority: {task['priority']})"
            self.task_listbox.insert(tk.END, task_text)
    
    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)
        messagebox.showinfo("Info", "Tasks saved successfully.")
    
    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []
        except json.JSONDecodeError:
            messagebox.showwarning("Warning", "Error loading tasks. Starting with an empty list.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
