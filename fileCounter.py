import os
import tkinter as tk
from tkinter import filedialog, messagebox

def is_hidden(filepath):
    # On Windows, hidden files have a hidden attribute
    # On Unix-like systems, they start with '.'
    name = os.path.basename(filepath)
    if os.name == 'nt':
        try:
            import ctypes
            attrs = ctypes.windll.kernel32.GetFileAttributesW(str(filepath))
            return attrs != -1 and (attrs & 2)
        except Exception:
            return False
    else:
        return name.startswith('.')

def count_files_in_repo(repo_path, ignore_hidden):
    file_count = 0
    for root, dirs, files in os.walk(repo_path):
        if ignore_hidden:
            # Filter out hidden directories
            dirs[:] = [d for d in dirs if not is_hidden(os.path.join(root, d))]
            # Filter out hidden files
            files = [f for f in files if not is_hidden(os.path.join(root, f))]
        file_count += len(files)
    return file_count

def choose_directory():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        path_var.set(folder_selected)

def count_files():
    path = path_var.get()
    if not os.path.isdir(path):
        messagebox.showerror("Error", "Please select a valid directory.")
        return

    ignore = ignore_hidden_var.get()
    count = count_files_in_repo(path, ignore)
    result_var.set(f"Total files: {count}")

# Set up the GUI
root = tk.Tk()
root.title("File Counter")

path_var = tk.StringVar()
ignore_hidden_var = tk.BooleanVar(value=True)
result_var = tk.StringVar()

tk.Label(root, text="Repository Folder:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
tk.Entry(root, textvariable=path_var, width=50).grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse...", command=choose_directory).grid(row=0, column=2, padx=5, pady=5)

tk.Checkbutton(root, text="Ignore hidden files/folders", variable=ignore_hidden_var).grid(row=1, column=0, columnspan=3, padx=5, pady=5)

tk.Button(root, text="Count Files", command=count_files).grid(row=2, column=1, pady=10)
tk.Label(root, textvariable=result_var, font=("Arial", 12, "bold")).grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()
