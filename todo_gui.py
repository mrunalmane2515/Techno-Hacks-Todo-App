import tkinter as tk
from tkinter import messagebox, simpledialog
import json

FILENAME = "tasks.json"
tasks = []

# ----------- File Handling ----------
def save_tasks():
    with open(FILENAME, "w") as file:
        json.dump(tasks, file)

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except:
        return []

# ----------- Actions ----------
def add_task():
    task = entry.get()
    deadline = deadline_entry.get()
    if task:
        tasks.append({"task": task, "completed": False, "deadline": deadline})
        update_listbox()
        save_tasks()
        entry.delete(0, tk.END)
        deadline_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
        save_tasks()
    except:
        messagebox.showwarning("Warning", "No task selected!")

def mark_completed():
    try:
        selected = listbox.curselection()[0]
        tasks[selected]["completed"] = True
        update_listbox()
        save_tasks()
    except:
        messagebox.showwarning("Warning", "No task selected!")

def edit_task():
    try:
        selected = listbox.curselection()[0]
        new_val = simpledialog.askstring("Edit Task", "Edit task:", initialvalue=tasks[selected]["task"])
        if new_val:
            tasks[selected]["task"] = new_val
            update_listbox()
            save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task first!")

def clear_completed():
    global tasks
    tasks = [t for t in tasks if not t["completed"]]
    update_listbox()
    save_tasks()

def update_listbox():
    listbox.delete(0, tk.END)
    for item in tasks:
        status = "✔️" if item["completed"] else "⏺"
        deadline = f" [Due: {item['deadline']}]" if item["deadline"] else ""
        listbox.insert(tk.END, f"{status} {item['task']}{deadline}")

# ----------- GUI Setup ----------
window = tk.Tk()
window.title("To-Do List App")
window.geometry("420x600")
window.config(bg="#f4f4f4")

frame = tk.Frame(window, bg="#ffffff", padx=15, pady=15, relief="groove", bd=2)
frame.pack(pady=15)

tk.Label(frame, text="Add Your Task", font=("Arial", 14, "bold"), bg="#ffffff").pack(pady=5)

entry = tk.Entry(frame, width=32, font=("Arial", 11))
entry.pack(pady=5)

deadline_entry = tk.Entry(frame, width=32, font=("Arial", 11))
deadline_entry.insert(0, "Optional Deadline")
deadline_entry.pack(pady=5)

tk.Button(frame, text="Add Task", width=20, bg="#4CAF50", fg="white", font=("Arial", 11), command=add_task).pack(pady=8)

# Task List Box Frame (Scrollable)
list_frame = tk.Frame(window)
list_frame.pack()

scroll = tk.Scrollbar(list_frame)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(list_frame, width=45, height=15, font=("Arial", 11), yscrollcommand=scroll.set)
listbox.pack(side=tk.LEFT, pady=10)
scroll.config(command=listbox.yview)

btn_frame = tk.Frame(window, bg="#f4f4f4")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Edit Task", width=18, bg="#2196F3", fg="white", command=edit_task).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Mark Completed", width=18, bg="#9C27B0", fg="white", command=mark_completed).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Remove Task", width=18, bg="#FF5722", fg="white", command=remove_task).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Clear Completed", width=18, bg="#795548", fg="white", command=clear_completed).grid(row=1, column=1, padx=5, pady=5)

tasks = load_tasks()
update_listbox()
window.mainloop()
