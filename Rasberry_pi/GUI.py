import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

upload = tk.Button(canvas, text="upload data", bg="#323333", fg="#ffffff"
                   , height=10, width=20)
upload.pack()
root.mainloop()




