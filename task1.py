"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""


import tkinter as tk 
from tkinter import *

win = tk.Tk()
win.geometry("300x200")

eoutput = StringVar()
eoutput.set("Output goes here")

def clickFunction(event):
    print(event)
    name = e1.get()
    number = e2.get()
    grade = e3.get()
    name = str(name)
    number = int(number)
    grade = int(grade)
    answer = (f"{name}, {number}, {grade}")

    a_entry.delete(0,END)
    a_entry.insert(0,answer)

l1 = Label(win, text="Enter name")
l2 = Label(win, text="Enter student number")
l3 = Label(win, text="Enter grade")

e1 = Entry(win, width=20)
e2 = Entry(win, width=20)
e3 = Entry(win, width=20)

b1 = Button(win, text="Click to display information")
b1.bind("<Button>",clickFunction)

a_entry = Entry(win, width=35, textvariable=eoutput)

l1.grid(row=1,column=1)
l2.grid(row=2,column=1)
l3.grid(row=3,column=1)
e1.grid(row=1,column=2)
e2.grid(row=2,column=2)
e3.grid(row=3,column=2)
b1.grid(row=4, column=1, columnspan=2)
a_entry.place(x=32,y=90)

win.mainloop()