"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients. For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""


import tkinter as tk 
from tkinter import *

win = tk.Tk()
win.geometry("400x400")

eoutput = StringVar()
eoutput.set("output")

def clickFunction(event):
    print(event)
    b = e1.get()
    c = e2.get()
    b = float(b)
    c = float(c)
    a = 1

    (a**2) + (2*a*b) + (b**2) = (a + b)**2
    (a**2) - (2*a*b) + (b**2) = (a - b)**2
    answer=(f"(X+{b})(X+{c})")

    a_entry.delete(0,END)
    a_entry.insert(0,answer)

instructions = Label(win, text='This calculator will factor your trinomial where the "A" value is "1".\nEnter values for "B" and "C"')

l1 = Label(win, text="Enter coefficient for B")
l2 = Label(win, text="Enter coefficient for C")

e1 = Entry(win, width=5)
e2 = Entry(win, width=5)

b1 = Button(win, text="Click to factor trinomial")
b1.bind("<Button>",clickFunction)

a_entry = Entry(win, width=10, textvariable=eoutput)

instructions.place(x=1,y=1)
l1.place(x=50,y=40)
l2.place(x=50,y=80)
e1.place(x=190,y=40)
e2.place(x=190,y=80)
b1.place(x=50,y=120)
a_entry.place(x=190,y=150)

win.mainloop()