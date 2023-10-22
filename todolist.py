import tkinter as tk

# Funtion to add the task 
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

# Function to remove the task from the list
def remove_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        pass

# Create a main window
def main():
    global entry, listbox
    root = tk.Tk()
    root.title("To-Do List")

# Create a entry field for task input
    entry = tk.Entry(root, width=50)
    entry.pack(pady=10)

# Create button to add the task    
    add_button = tk.Button(root, text="Add Task", command=add_task)
    add_button.pack(pady=5)

# Create button to remove the task from the list
    remove_button = tk.Button(root, text="Remove Task", command=remove_task)
    remove_button.pack(pady=5)

# Create a listbox for the task
    listbox = tk.Listbox(root, width=50)
    listbox.pack(pady=10)

# Run the application
    root.mainloop()
if __name__ == "__main__":
    main()


