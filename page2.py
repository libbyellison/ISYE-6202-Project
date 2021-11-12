# import the modules
import tkinter
from tkinter import *
from tkinter import ttk
import random
from tkinter.messagebox import showinfo
from PIL import ImageTk,Image  

def login_clicked():
    """ callback when the login button clicked
    """
    msg = f'Welcome to your first day, {playername.get()}!'
    showinfo(
        title='Welcome to the game!',
        message=msg
    )
    print(playername.get())


# Driver Code

# create a GUI window
root = tkinter.Tk()
def nextPage():
    root.destroy()
    import page2
# set the title
root.title("Warehouse Simulation Game")

# set the size
root.geometry("1000x1000")

root.columnconfigure(0,weight = 1)
root.columnconfigure(1,weight = 1)
root.columnconfigure(2,weight = 1)

# add an instructions label
instructions = tkinter.Label(root, text = "Background Year1",
                                                      font = ('Tahoma', 20))
instructions.grid(column=1, row=0, padx=5, pady=5)




# start the GUI
root.mainloop()
