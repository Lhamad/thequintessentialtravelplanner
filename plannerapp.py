#Creating a window using tinker
from tkinter import *
from tkinter import simpledialog
from tkinter import ttk
from math import *
from tkinter.messagebox import *
from datetime import date
from tkinter.font import Font
import tkinter as tk
import datetime
import pytz









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

#datetime

Label(tab1,text="Please choose your current timezone").pack(side=LEFT, padx=5)


OPTIONS = [
'US/Eastern',
'America/Chicago',
'America/Los_Angeles'
] #etc



variable = StringVar(tab1)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(tab1, variable, *OPTIONS)
w.pack(side=LEFT, padx=5)

now_utc = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)

def ok():
    fmt = '%H:%M'
    
    source_time_zone = pytz.timezone(variable.get())
    local_time = source_time_zone.normalize(now_utc.astimezone(source_time_zone))
    local_time_formatted=local_time.strftime(fmt)
    blank2.insert(0, local_time_formatted)

    Japan_timezone = pytz.timezone('Japan')
    Japan_local_time = Japan_timezone.normalize(now_utc.astimezone(Japan_timezone))
    
    
    Japan_local_time_formatted=Japan_local_time.strftime(fmt)
    blank1.insert(0, Japan_local_time_formatted)

button = Button(tab1, text="OK", command=ok)
button.pack(side=LEFT, padx=5)

Label(tab1, text="Current Local Time:").pack(side=LEFT,padx=5)
blank2=Entry(tab1)
blank2.pack(side=LEFT, padx=5)


Label(tab1, text="Current Time in Japan").pack(side=LEFT, padx=5)
blank1=Entry(tab1)
blank1.pack(side=LEFT, padx=5)









#Currency Conversion - located on tab 2

def show_answer():
    Ans = float(num1.get()) * 103.23
    blank.insert(0, Ans)



Label(tab2, text = "Enter USD:").pack(side=LEFT, padx=5)
num1 = Entry(tab2)
num1.pack(side=LEFT, padx=5)

Button(tab2, text='Show', command=show_answer).pack(side=LEFT, padx=5)

Label(tab2, text = "Amount in Yen:").pack(side=LEFT, padx=5)
blank = Entry(tab2)
blank.pack(side=LEFT, padx=5)





root.mainloop()


