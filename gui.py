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
import glob
import sys
from tkinter import Text, Tk
window = tk.Tk()
 
window.title("Manage Sites")
 
window.geometry('1000x1000')

window.configure(background="gray")


bg_image = PhotoImage(file ="indexxx.png")
x = Label (image = bg_image,borderwidth=0)

x.place(x=10,y=10)



lbl = Label(window, text="Add group :",background="gray",foreground="white")
lbl.config(width=200)
lbl.config(font='Helvetica  20 bold')
lbl.place(x=250, y=300)
 
t = Text(window, height=2, width=40,background="white")
t.place(x=440, y=310)


def addGroup():
    fileName = t.get('1.0', END)
    filepath=os.path.join("file_directory",fileName)
    if os.path.isfile(filepath)==True:
        messagebox.showwarning('Warning', 'File exists')
        exit
    
    f = open(filepath, "a")

    f.close

btn = tk.Button(window, text="Add File", command=addGroup)
btn.config( height =2, width = 8 )
btn.place(x=745, y=310)

"""*********************************************************************"""
lbl2 = Label(window, text="Select Group :",background="gray",foreground="white")
lbl2.config(width=200)
lbl2.config(font='Helvetica 20 bold')
lbl2.place(x=250, y=550)


combo = Combobox(window, height=2, width=35,background="yellow")
combo.place(x=450, y=565)

for filenames in  os.walk("file_directory"):
    for file in filenames:
      combo['values']=file



def openFile():
    fileName=combo.get()

    filepath=os.path.join("file_directory",fileName)
    print(filepath)
   
    programName="gedit"
    sp.Popen([programName,filepath])



btn2 = tk.Button(window, text="Open File", command=openFile)
btn2.config( height =2, width = 8 )
btn2.place(x=750, y=550)   
    
          
window.mainloop()



