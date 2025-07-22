import tkinter as tk
from tkinter import filedialog
import compressor
import os

def compress():
    path = filedialog.askopenfilename()
    if path:
        output = path + ".compressed"
        mycompressor.compress_file(path, output)
        print(f"Compressed to: {output}")

def decompress():
    path = filedialog.askopenfilename()
    if path:
        output = os.path.splitext(path)[0] + ".decompressed"
        mycompressor.decompress_file(path, output)
        print(f"Decompressed to: {output}")

root = tk.Tk()
root.title("File Compressor")

tk.Button(root, text="Compress File", command=compress).pack(pady=10)
tk.Button(root, text="Decompress File", command=decompress).pack(pady=10)

root.mainloop()
