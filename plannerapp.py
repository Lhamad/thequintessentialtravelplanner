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
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import json







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
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Mainpage') 
tabControl.add(tab2, text ='Budget') 
tabControl.add(tab3, text ='Address Book') 

tabControl.pack(expand = 1, fill ="both") 

#datetime

#Countdown to your vacation

def countdown():
    fmt1 = '%D'
    current_date=datetime.datetime.now()
    year, month, day=map(int,blank3.get().split(','))
    vacation_day=datetime.datetime(year,month,day)
    countdown_days=(vacation_day-current_date)
    countdown_days_formated=countdown_days.days
    blank4.insert(0, countdown_days_formated)


Label(tab1, text="What day is your vacation.  Enter in form YYYY,MM,DD").pack(side=TOP, pady=10)
blank3=Entry(tab1)
blank3.pack(side=TOP)

button = Button(tab1, text="Countdown", command=countdown)
button.pack(side=TOP, padx=5)

Label(tab1, text="Number of Days until your vacation: ").pack(side=TOP, pady=10)

blank4=Entry(tab1)
blank4.pack(side=TOP)

#Converting from your current time zone to Japanese time Zone
Label(tab1,text="Please choose your current timezone").pack(side=LEFT, padx=5, pady=20)


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





Button(tab2, text='Show', command=show_answer).pack(side=BOTTOM, padx=5)


blank = Entry(tab2)
blank.pack(side=BOTTOM, padx=5)

Label(tab2, text = "Amount in Yen:").pack(side=BOTTOM, padx=5)

num1 = Entry(tab2)
num1.pack(side=BOTTOM, padx=5)

Label(tab2, text = "Enter USD:").pack(side=BOTTOM, padx=5)


#Pie Chart

Label(tab2, text = "What is your food budget?:").pack(side=TOP, padx=5)
food_budget = Entry(tab2)
food_budget.pack(side=TOP, pady=5)

Label(tab2, text = "What is your travel budget?:").pack(side=TOP, padx=5)
travel_budget = Entry(tab2)
travel_budget.pack(side=TOP, pady=5)

Label(tab2, text = "What is your entertainment budget?:").pack(side=TOP, padx=5)
entertainment_budget = Entry(tab2)
entertainment_budget.pack(side=TOP, pady=5)

Label(tab2, text = "What is your shopping budget?:").pack(side=TOP, padx=5)
shopping_budget = Entry(tab2)
shopping_budget.pack(side=TOP, pady=5)

def piechart():
    global food_budget
    global travel_budget
    global entertainment_budget
    global shopping_budget

    global pie2

    food_budget1=float(food_budget.get())
    travel_budget1=float(travel_budget.get())
    entertainment_budget1=float(entertainment_budget.get())
    shopping_budget1=float(shopping_budget.get())

    figure2 = Figure(figsize=(4,3), dpi=100) 
    subplot2 = figure2.add_subplot(111) 
    labels2 = 'Food', 'Travel', 'Entertainment', 'Shopping'
    pieSizes = [float(food_budget1),float(travel_budget1),float(entertainment_budget1),float(shopping_budget1)]
    my_colors2 = ['lightblue','lightsteelblue','silver','red']
    explode2 = (0, 0.1, 0,0)  
    subplot2.pie(pieSizes, colors=my_colors2, explode=explode2, labels=labels2, autopct='%1.1f%%', shadow=True, startangle=90) 
    subplot2.axis('equal')  
    pie2 = FigureCanvasTkAgg(figure2, tab2)
    pie2.get_tk_widget().pack()



Button(tab2, text='Calculate', command=piechart).pack(side=TOP, pady=5)

#addressbook

#this section allows people to input the address and name of the place and then puts that information into a dictionary

addressbook={}
def addressbookuserinput():
    useradded={str(nameofplace.get()):str(addressofplace.get())}
    addressbook.update(useradded)
    with open ('addressbook.json','w') as f:
        f.write(json.dumps(addressbook))
   
    
    

Label(tab3, text = "Enter Name of Place of Interest:").grid(row=0, column=0)
Label(tab3, text = "Enter Address of Place:").grid(row=0, column=2)


nameofplace = Entry(tab3)
nameofplace.grid(row=0, column=1)

addressofplace = Entry(tab3)
addressofplace.grid(row=0, column=3)

Button(tab3, text='Add to address book', command=addressbookuserinput).grid(row=0, column=4, sticky=W,)


#This is where the user can put an address into the entry and the program will spit out a address
userneededaddress=Entry(tab3)
userneededaddress.grid(row=1, column=1)

addressofuserinput=Entry(tab3)
addressofuserinput.grid(row=2, column=2)

Label(tab3, text="The address of the requested place is: ").grid(row=2, column=1)
Label(tab3, text="Enter Name of Place you would like an address for: ").grid(row=1, column=0)

def search_entry(): 
   s=open('addressbook.json','r').read()
   if userneededaddress.get() in s:
       y=str(addressbook[userneededaddress.get()])
       addressofuserinput.insert(0, y)
       
   else:
       addressofuserinput.insert(0, "Not in Book")
    
    
    #this creates a new label to the GUI
    

Button(tab3, text='search_entry', command=search_entry).grid(row=1, column=2)




root.mainloop()


