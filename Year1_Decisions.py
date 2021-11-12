# import the modules
import tkinter
from tkinter import *
from tkinter import ttk
import random
from tkinter.messagebox import showinfo
#
# Driver Code

# create a GUI window
root = tkinter.Tk()
def button_clicked():
    root.destroy()
    import Year1_Results
# set the title
root.title("Warehouse Simulation Game")

# set the size
root.geometry("1000x1000")

root.columnconfigure(0,weight = 1)
root.columnconfigure(1,weight = 1)
root.columnconfigure(2,weight = 1)

# add an instructions label
instructions = tkinter.Label(root, text = "Player 1 Makes Year 1 Decisions",
                                                      font = ('Tahoma', 20))
instructions.grid(column=1, row=0, padx=5, pady=5)

next_button = tkinter.Button(root, text="Click Here to Continue", command=button_clicked)
next_button.grid(column=1, row=1, padx=5, pady=5)

# start the GUI
root.mainloop()
