from tkinter import *
import os.path
from tkinter import messagebox
import os
import os.path
from tkinter.ttk import *
from os import listdir
import subprocess as sp
 
window = Tk()
 
window.title("Manage Sites")
 
window.geometry('1000x1000')

window.configure(background="white")


bg_image = PhotoImage(file ="images.png")

x = Label (image = bg_image)

x.grid(row = 0, column = 0)



lbl = Label(window, text="Add group :", font=30,background="white")
 
lbl.grid(column=0, row=1)
 
txt = Entry(window,width=20)
 
txt.grid(column=3, row=1)


def addGroup():
 
    fileName = txt.get()
    filepath=os.path.join("file_directory",fileName)
    if os.path.isfile(filepath)==True:
        messagebox.showwarning('Warning', 'File exists')
        exit
    
    f = open(filepath, "a")

    f.close

btn = Button(window, text="ADD", command=addGroup)
btn.grid(column=4, row=1)

"""*********************************************************************"""

combo = Combobox(window)
combo.grid(column=3, row=2)

for filenames in  os.walk("file_directory"):
    for file in filenames:
      combo['values']=file


def openFile():
    fileName=combo.get()

    filepath=os.path.join("file_directory",fileName)
    print(filepath)
   
    programName="gedit"
    sp.Popen([programName,filepath])
    
    
lb= Label(window, text="open group :",font=30,background="white")

lb.grid(column=0, row=2)

button = Button(window, text="OPEN", command=openFile)

button.grid(column=4, row=2)

window.mainloop()


