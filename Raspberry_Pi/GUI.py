import tkinter as tk
from tkinter import *


import update_bigquery


def upload(temp, pressure, humidity, tableInput):
    update_bigquery.updateTable(tableInput, temp, pressure, humidity)


def init():
    root = tk.Tk()
    Label(root, text="Temperature: ").grid(row=0, column=0)
    tempInput = Entry(root, width=20,)
    tempInput.grid(row=0, column=1, pady=10)

    Label(root, text="Pressure: ").grid(row=1, column=0)
    pressureInput = Entry(root, width=20,)
    pressureInput.grid(row=1, column=1, pady=10)

    Label(root, text="Humidity: ").grid(row=2, column=0)
    humidityInput = Entry(root, width=20,)
    humidityInput.grid(row=2, column=1, pady=10)

    Label(root, text="Table id: ").grid(row=3, column=0)
    tableInput = Entry(root, width=20, )
    tableInput.grid(row=3, column=1, pady=10)

    def buttonPress():
        temp = tempInput.get()
        pressure = pressureInput.get()
        humidity = humidityInput.get()
        table = tableInput.get()
        upload(temp, pressure, humidity, table)

    uploadButton = tk.Button(root, text="upload data", bg="#323333", fg="#ffffff",
                             height=1, width=20, command=buttonPress)
    uploadButton.grid(row=4, column=0, columnspan=2, pady=10)

    root.mainloop()


init()




