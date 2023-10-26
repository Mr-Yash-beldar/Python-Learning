import tkinter as tk
from tkinter import IntVar,messagebox,Radiobutton
screen = tk.Tk()
screen.title("Yashodip Beldar")
screen.geometry('200x200')  # Corrected the size format
def viewSelected():
    choice=var.get()
    if choice==1:
        output="science"
    elif choice==2:
        output="Commarce"
    elif choice==3:
        output="Arts"
    else:
        output="Invalid Input"

    return messagebox.showinfo('Yashodip Beldar',f"Your Selected {output}")

var=IntVar()
Radiobutton(screen, text="Science", variable=var, value=1, command=viewSelected).grid(row=0,stick='w')
Radiobutton(screen, text="Commarce", variable=var,value=2, command=viewSelected).grid(row=1,stick='w')
Radiobutton(screen, text="Arts", variable=var, value=3, command=viewSelected).grid(row=2,stick='w')
screen.mainloop()