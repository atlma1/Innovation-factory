# from sense_hat import SenseHat
from update_bigquery import updateTable
import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox

def guiInit():
    root = tk.Tk()

    # table input
    Label(root, text="Table id: ").grid(row=0, column=0)
    tableInput = Entry(root, width=20, )
    tableInput.grid(row=0, column=1, pady=8)

    #delay input
    Label(root, text="choose delay: ").grid(row=1, column=0)
    delayInput = Entry(root, width=20, )
    delayInput.grid(row=1, column=1, pady=8)

    def envSense(delay, table):
        sense = SenseHat()
        timeSince = 0
        while True:
            # checks the environment
            humidity = sense.get_humidity()
            temperature = sense.get_temperature()
            pressure = sense.get_pressure()
            # adds to table
            errors = updateTable(table, temperature, pressure, humidity, timeSince)
            if not errors:
                print('Rows have been added')
            else:
                print(f'Encountered errors while inserting rows: <errors>')
            time.sleep(delay)
            timeSince += delay


    def joystickSense(table):
        sense = SenseHat()

        while True:
            event = sense.stick.wait_for_event()
            if event.direction == "up":
                print("step completed")
            elif event.direction == "down":
                print("step failed")
            elif event.direction == "middle":
                print("tool completed")


    # stuff for choosing whether to use joystick or environment sensing
    var1 = IntVar()

    def chooseMode(value):

        def environment():
            print("environment selected")
            if len(delayInput.get()) == 0 or len(delayInput.get()) == 0:
                messagebox.showerror("Delay and table must be specified")
                exit(1)
            else:
                envSense(delayInput.get(), tableInput.get())

        def joystick():
            print("joystick selected")

        if value == 1:
            runButton = Button(root, text="Run", bg="#323333", fg="#ffffff",
                               height=1, width=20, command=environment)
            runButton.grid(row=5, column=0, columnspan=2, pady=10)
        else:
            runButton = Button(root, text="Run", bg="#323333", fg="#ffffff",
                               height=1, width=20, command=joystick)
            runButton.grid(row=5, column=0, columnspan=2, pady=10)

    environmentSelect = Radiobutton(root, text="environment detection", variable=var1,
                                    value=1, command=lambda: chooseMode(1))
    environmentSelect.grid(row=3, column=0, pady=8, columnspan=2)

    joystickSelect = Radiobutton(root, text="joystick detection", variable=var1,
                                 value=2, command=lambda: chooseMode(2))
    joystickSelect.grid(row=4, column=0, pady=8, columnspan=2)

    root.mainloop()




guiInit()
