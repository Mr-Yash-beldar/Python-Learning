import tkinter as tk
from tkinter import messagebox

def save_data():
    result = messagebox.askyesno("Confirmation", "Do you want to save the data?")
    if result:
        # Save the data or perform some action
        print("Data saved.")
    else:
        # Data not saved
        print("Data not saved.")

def check_and_save():
    # You can add your check logic here
    # For this example, let's assume the check is not passed
    if False:  # Replace 'False' with your actual condition
        messagebox.showerror("Error", "The check failed. Data cannot be saved.")
    else:
        save_data()

screen = tk.Tk()
screen.title("Yashodip Beldar")
screen.geometry('200x200')

button = tk.Button(screen, text="Check and Save", command=check_and_save)
button.pack(padx=50, pady=50)

screen.mainloop()
