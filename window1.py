import tkinter as tk
from tkinter import *
class Interface0:
    def __init__(self, master):
        self.master = master
        self.master.title("SoloScan")
        self.master.geometry("400x400")
        self.master.resizable(0, 0)
        self.frame = tk.Frame(self.master, bg="black")
        #self.frame.title("SoloScan")
        self.text = Label(self.frame, text = 'SoloScan',fg='yellow', bg ='black',font =(
          'Verdana', 15)).pack(side = TOP, pady = 10)
        self.text3 = Label(self.frame,text="Scan itttttt!!!!!",fg='yellow', bg ='black').pack(side=TOP)
        photo1 = PhotoImage(file ="/home/thor/Desktop/FYP_Final/images.png")
        self.button = Label(self.frame,text="Choose File",image=photo1).pack(side = TOP)
        self.text1= Label(self.frame,text="Drag files to load images or",fg='yellow', bg ='black').pack(side = TOP, pady = 10)
        self.b1 = Button(self.frame,text="Choose File",fg='yellow', bg ='black').pack(side = TOP, pady = 10)
        self.butnew("Next",Interface1)
        self.frame.pack()

    def butnew(self, text, _class):
            tk.Button(self.frame, text = text, command= lambda: self.new_window(_class)).pack()

    def new_window(self, _class):
        self.Interface1 = tk.Toplevel(self.master)
        _class(self.Interface1)

class Interface1(Interface0):
    def __init__(self, master):
        self.master = master
        self.master.title("Second Window")
        self.master.geometry("400x400")
        self.master.resizable(0, 0)
        self.show_Model()

    def show_Model(self):

        self.frame = tk.Frame(self.master, bg="black")
        self.text = Label(self.frame, text = 'SoloScan',fg='yellow', bg ='black',font =('Verdana', 15)).pack(side = TOP, pady = 10)
        self.text3 = Label(self.frame,text="Choose any :",fg='yellow', bg ='black')
        self.b1 = Button(self.frame,text="Feature Detection",fg='yellow', bg ='black',height = 2, width = 36).pack(side = TOP, pady = 10)
        self.b2 = Button(self.frame,text="Keypoints matching",fg='yellow', bg ='black',height = 2, width = 36).pack(side = TOP, pady = 10)
        self.b3 = Button(self.frame,text="Show Triangulation",fg='yellow', bg ='black',height = 2, width = 36).pack(side = TOP, pady = 10)
        self.b4 = Button(self.frame,text="Display 3D Point Cloud",fg='yellow', bg ='black',height = 2, width = 36).pack(side = TOP, pady = 10)
        self.text2 = Button(self.frame,text="Exit",command=self.close_window).pack(side = LEFT)

        self.butnew("Back",Interface0)
        #self.text3 = Button(self.frame,text="Back",fg='yellow', bg ='black',width = 10,command=self.Previous_window).pack(side = LEFT, pady = 20)
        self.frame.pack()

    def butnew(self, text, _class):
            tk.Button(self.frame, text = text, command= lambda: self.pre_window(_class)).pack(side = RIGHT)

    def Previous_window(self,_class):

        self.Interface0 = tk.Toplevel(self.master)
        _class(self,self.Interface0)

    def close_window(self):
        self.master.destroy()
root = tk.Tk()
app = Interface0(root)
root.mainloop()
