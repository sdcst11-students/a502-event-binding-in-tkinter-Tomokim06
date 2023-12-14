#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""


import tkinter as tk 
from tkinter import *

win = tk.Tk()
win.geometry("225x110")

eoutput = StringVar()
eoutput.set("Hypotenuse is...")

def clickFunction(event):
    print(event)
    firstside = e1.get()
    secondside = e2.get()
    firstside = float(firstside)
    secondside = float(secondside)
    answer = round(((firstside**2)+(secondside**2))**0.5, 2)

    a_entry.delete(0,END)
    a_entry.insert(0,answer)

l1 = Label(win, text="Enter 1st side")
l2 = Label(win, text="Enter 2nd side")

e1 = Entry(win, width=20)
e2 = Entry(win, width=20)

b1 = Button(win, text="Click to find hypotneuse side length")
b1.bind("<Button>",clickFunction)

a_entry = Entry(win, width=20, textvariable=eoutput)

l1.grid(row=1,column=1)
l2.grid(row=2,column=1)
e1.grid(row=1,column=2)
e2.grid(row=2,column=2)
b1.grid(row=4, column=1, columnspan=2)
a_entry.grid(row=5, column=2)

win.mainloop()