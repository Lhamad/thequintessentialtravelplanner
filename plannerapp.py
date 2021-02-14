#Creating a window using tinker
from tkinter import *
from tkinter import simpledialog
from tkinter import ttk
from math import *
from tkinter.messagebox import *
from datetime import date
from tkinter.font import Font
import tkinter as tk

root = Tk()
root.geometry("1200x950")
frame = Frame(root)
frame.pack()

leftframe = Frame(root)
leftframe.pack(side=LEFT)
 
rightframe = Frame(root)
rightframe.pack(side=RIGHT)

topframe = Frame(root)
topframe.pack(side=TOP)



#create tabs
tabControl = ttk.Notebook(root) 

tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Mainpage') 
tabControl.add(tab2, text ='Budget') 

tabControl.pack(expand = 1, fill ="both") 
#Currency Conversion - located on tab 2

def show_answer():
    Ans = float(num1.get()) * 103.23
    blank.insert(0, Ans)



Label(tab2, text = "Enter USD:").grid(row=0)
Label(tab2, text = "Amount in Yen:").grid(row=1)

#these are the open areas the user can put stuff in
num1 = Entry(tab2)
blank = Entry(tab2)


num1.grid(row=0, column=1)
blank.grid(row=1, column=1)

Button(tab2, text='Show', command=show_answer).grid(row=4, column=1, sticky=W, pady=4)



root.mainloop()


