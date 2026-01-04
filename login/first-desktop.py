import tkinter as tk
from tkinter import messagebox

root = tk.Tk()  # Create the main window
root.title("To-Do List")  # Set window title
root.geometry("600x800")  # Set window size

tasks = []  # List to store tasks

def add_task():
    """Adds a task to the list."""
    task = task_entry.get()  # Get task from the entry field
    if task:
        tasks.append(task)  # Add task to the list
        task_listbox.insert(tk.END, task)  # Display task in the listbox
        task_entry.delete(0, tk.END)  # Clear input field
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")  # Show warning if input is empty
        
def remove_task():
    """Removes selected task from the list."""
    try:
        selected_task_index = task_listbox.curselection()[0]  # Get index of selected task
        task_listbox.delete(selected_task_index)  # Remove task from listbox
        del tasks[selected_task_index]  # Remove task from the list
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")  # Show warning if no task is selected
        
# Input field for entering tasks
task_entry = tk.Entry(root, width=100)
task_entry.pack(pady=10)

# Buttons to add and remove tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=40, height=15)
task_listbox.pack(pady=10)
    
root.mainloop()  # Start the application    