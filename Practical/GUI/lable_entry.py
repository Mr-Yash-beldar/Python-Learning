from tkinter import *
screen=Tk()
Label(screen,text="First Name").grid(row=0,sticky='w')
Label(screen,text="Last Name").grid(row=1,sticky='w')
element1=Entry(screen)
element2=Entry(screen)
screen.geometry('400x400')  
element1.grid(row=0,column=1)
element2.grid(row=1,column=1)
screen.mainloop()

