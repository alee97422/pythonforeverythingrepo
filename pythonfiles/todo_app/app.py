import tkinter as tk
import ttkbootstrap as ttk

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)

def clear_all():
    task_list.delete(0, tk.END)

root = ttk.Window(themename="vapor")
root.title("To-Do List")

label = tk.Label(root, text="To-Do List", font=("Helvetica", 16))
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

task_list = tk.Listbox(root, selectmode=tk.SINGLE)
task_list.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

clear_button = tk.Button(root, text="Clear All", command=clear_all)
clear_button.pack()

root.mainloop()
