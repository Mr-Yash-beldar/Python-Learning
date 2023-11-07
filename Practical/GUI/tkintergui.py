import tkinter as tk

screen = tk.Tk()
screen.title("Yashodip Beldar")
button = tk.Button(screen, text="Stop", width=25, command=screen.destroy)
screen.geometry('400x400')  # Corrected the size format
button.pack(side='top', padx=50, pady=50)  # Changed 'padx' to 'pady'
screen.mainloop()
