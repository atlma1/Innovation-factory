import tkinter as tk
from tkinter import filedialog, Text
from tkinter import END
from tkinter import Entry
from tkinter import *
import os

import StreamToBigQuery
root = tk.Tk()

temp = 0.0
pressure = 0.0
humidity = 0.0






def upload(temp, pressure, humidity):
    StreamToBigQuery.updateTable(StreamToBigQuery.Table, temp, pressure, humidity)

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

temp = Canvas(canvas)
tempLabel = Label(temp, text="Temperature")
tempLabel.pack(side=LEFT)
tempInput = Entry(temp, width=20, text="temperature")
tempInput.pack()



def foo():
    input = tempInput.get()
    print(input)

upload = tk.Button(canvas, text="upload data", bg="#323333", fg="#ffffff"
                   , height=10, width=20, command=foo)



upload.pack()
root.mainloop()




