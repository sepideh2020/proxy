from tkinter import *
import os.path
from tkinter import messagebox
import os
import os.path
from tkinter.ttk import *
from os import listdir
import subprocess as sp
import tkinter as tk
from math import *

window = tk.Tk()
 
window.title("Manage Sites")
 
window.geometry('1000x1000')

window.configure(background="white")


bg_image = PhotoImage(file ="images.png")

x = Label (image = bg_image,borderwidth=0)

x.grid(row = 0, column = 0)



lbl = Label(window, text="Add group :", font=30,background="white")
 
lbl.grid(column=1, row=6)
 
txt = Entry(window,width=20)
 
txt.grid(column=3, row=6)


def addGroup():
 
    fileName = txt.get()
    filepath=os.path.join("file_directory",fileName)
    if os.path.isfile(filepath)==True:
        messagebox.showwarning('Warning', 'File exists')
        exit
    
    f = open(filepath, "a")

    f.close

btn = Button(window, text="ADD", command=addGroup)
btn.grid(column=4, row=6)

"""*********************************************************************"""
lb= Label(window, text="open group :",font=30,background="white",justify = 'center)

lb.grid(column=1, row=8)

combo = Combobox(window)
combo.grid(column=3, row=8)

for filenames in  os.walk("file_directory"):
    for file in filenames:
      combo['values']=file


def openFile():
    fileName=combo.get()

    filepath=os.path.join("file_directory",fileName)
    print(filepath)
   
    programName="gedit"
    sp.Popen([programName,filepath])
    
    
button = Button(window, text="OPEN", command=openFile)

button.grid(column=4, row=8)



"""**************************************************************************"""


def choose():
    # for value (1&2) just put in what you need for it
    # for example, I just put a string '101' and '102' in value1 & 2
    # the control variable cb(n)_v would hold 1 if its checked and 0 if not

    result = []
    if cb1_v == 1:
        result.append(value1)
    if cb2_v == 1:
        result.append(value2)
    return result


i=0
for file in  os.walk("file_directory"):
        print(file)
              
        cb = tk.Checkbutton(window, text=file, variable=tk.IntVar())
        cb.grid(row=0,column=i)
        i=i+1
        
        
        btn1=tk.Button(window, text='Choose',command=choose)
        
        

btn1.grid(row=2, column=0)


window.mainloop()



