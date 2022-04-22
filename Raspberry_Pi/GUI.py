import tkinter as tk
from tkinter import *
from google.cloud import bigquery
import update_bigquery


def init():
    root = tk.Tk()

    # table input
    Label(root, text="Table id: ").grid(row=0, column=0)
    tableInput = Entry(root, width=20, )
    tableInput.grid(row=0, column=1, pady=8)
    # temperature input
    Label(root, text="Temperature: ").grid(row=1, column=0)
    tempInput = Entry(root, width=20, )
    tempInput.grid(row=1, column=1, pady=10)
    # pressure input
    Label(root, text="Pressure: ").grid(row=2, column=0)
    pressureInput = Entry(root, width=20, )
    pressureInput.grid(row=2, column=1, pady=10)
    # humidity input
    Label(root, text="Humidity: ").grid(row=3, column=0)
    humidityInput = Entry(root, width=20, )
    humidityInput.grid(row=3, column=1, pady=10)

    # call to update table
    def upload(temp, pressure, humidity, tableInput):
        update_bigquery.updateTable(tableInput, temp, pressure, humidity, None)

    # calls input and executes update
    def uploadButtonPress():
        temp = tempInput.get()
        pressure = pressureInput.get()
        humidity = humidityInput.get()
        table = tableInput.get()
        print("Added row\n temp:" + temp + "\n pressure:" + pressure + "\n humidity:" + humidity
              + "\n To table " + table)
        upload(temp, pressure, humidity, table)

    # upload button
    uploadButton = tk.Button(root, text="upload data", bg="#323333", fg="#ffffff",
                             height=1, width=20, command=uploadButtonPress)
    uploadButton.grid(row=4, column=0, columnspan=2, pady=10)

    def clearTable():
        client = bigquery.Client()
        query = "DELETE FROM " + tableInput.get() + " WHERE true"
        print("clearing table")
        queryResult = client.query(query)
        if queryResult.errors != NONE:
            try:
                queryResult.result()
            except:
                print("Bigquery only allows deleting or updating new data 30 minutes after it has been update"
                      "please try again in 30 or more minutes later")
        else:
            print(queryResult.errors)

    clearButton = tk.Button(root, text="clear table", bg="#323333", fg="#ffffff",
                            height=1, width=20, command=clearTable)
    clearButton.grid(row=5, column=0, columnspan=2, pady=10)

    root.mainloop()


init()
