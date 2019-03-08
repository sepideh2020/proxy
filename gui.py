from tkinter import *
import os.path
from tkinter import messagebox
import os
import os.path
from tkinter.ttk import *
from os import listdir
import subprocess as sp
 
window = Tk()
 
window.title("filter site")
 
window.geometry('1000x1000')

lbl = Label(window, text="add group :", font=30)
 
lbl.grid(column=1, row=1)
 
txt = Entry(window,width=20)
 
txt.grid(column=3, row=1)
 
def clicked():
 
    #res = txt.get()
    fileName = txt.get()

    if os.path.isfile(fileName)==True:
        messagebox.showwarning('Warning', 'File exists')
        exit
        
    #f=open("filtered.txt","a+")
    #f=open(fileName,"a+")
    filepath=os.path.join("file_directory",fileName)
    f = open(filepath, "a")
    #f.write(res + '\n')
    #print()
    
    f.close

btn = Button(window, text="ADD", command=clicked)
btn.grid(column=4, row=1)


combo = Combobox(window)

for filenames in  os.walk("file_directory"):
    for file in filenames:
      combo['values']=file

combo.grid(column=0, row=10)

def openFile():
    fileName=combo.get()

    filepath=os.path.join("file_directory",fileName)
    print(filepath)
    #file=open(filepath,"t")
    programName="gedit"
    sp.Popen([programName,filepath])
    
    

button = Button(window, text="ADD", command=openFile)
button.grid(column=0, row=11)




window.mainloop()

