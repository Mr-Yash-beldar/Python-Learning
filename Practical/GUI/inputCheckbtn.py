from tkinter import *

screen = Tk()
screen.title("Input and check button")
var1=IntVar()
Checkbutton(screen,text='male',activebackground='red',activeforeground='blue',variable=var1).grid(row=0,sticky=W)
var2=IntVar()
Checkbutton(screen,text='male',activebackground='red',activeforeground='green',variable=var2).grid(row=1)
screen.mainloop()
