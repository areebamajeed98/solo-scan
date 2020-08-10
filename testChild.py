import tkinter
from tkinter import *
window = Tk()
window.title("SoloScan")
window.configure(background="black")
text = Label(window, text = 'SoloScan',fg='yellow', bg ='black',font =(
  'Verdana', 15)).pack(side = TOP, pady = 10)
text3 = Label(text="Scan itttttt!!!!!",fg='yellow', bg ='black').pack(side=TOP)
photo = PhotoImage(file = "t.gif")

button = Label(text="Choose File",image =photo).pack(side = TOP, pady = 10)
text1= Label(text="Drag files to load images or",fg='yellow', bg ='black').pack(side = TOP, pady = 10)
b1 = Button(text="Choose File",fg='yellow', bg ='black').pack(side = TOP, pady = 10)
text2 = Button(text="Next",fg='yellow', bg ='black').pack(side = RIGHT, pady = 15)
window.mainloop()
