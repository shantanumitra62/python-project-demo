import matplotlib
matplotlib.use('Agg')
# tkinter is the standard GUI package in python 
from tkinter import *
from tkinter.ttk import Combobox
class tinkerDemo {
 global window=Tk()
var = StringVar()
var.set("Hello")
data = ("Hello", "Namaste", "Kon'nichiwa")
cb = Combobox(window, values=data)
cb.place(x=60, y=150)

lb=Listbox(window, height=5, selectmode='multiple')
for num in data:
    lb.insert(END,num)
    lb.place(x=250, y=150)




    
}




