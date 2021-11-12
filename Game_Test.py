# import the modules
import tkinter
from tkinter import *
from tkinter import ttk
import random
from tkinter.messagebox import showinfo
import PIL
from PIL import ImageTk,Image  


def login_clicked():
    """ callback when the login button clicked
    """
    msg = f'Welcome to your first day, {playername.get()}'
    showinfo(
        title='Welcome to the game!',
        message=msg
    )
    nextPage()
    print(playername.get())


# Driver Code

# create a GUI window
root = tkinter.Tk()
def nextPage():
    root.destroy()
    import Year1_BG
# set the title
root.title("Warehouse Simulation Game")

# set the size
root.geometry("1000x1000")

root.columnconfigure(0,weight = 1)
root.columnconfigure(1,weight = 1)
root.columnconfigure(2,weight = 1)
# Read the Image
image = Image.open("/Users/libbyellison/Desktop/6202 Game -  V1/buzz.jpg")
 
# Resize the image using resize() method
resize_image = image.resize((100,100))
 
img = ImageTk.PhotoImage(resize_image)
 
# create label and add resize image
label1 = Label(image=img)
label1.image = img

label1.grid(column=0, row=0, padx=5, pady=5)

  


# add an instructions label
instructions = tkinter.Label(root, text = "Welcome to the your first day as the Warehouse Manager."
											"\nYou will go through 5 years of running our\n Georgia Tech Bookstore Warehouse."
											"\nIf you do not make 10 million dollars, you will be fired."
											"\nApply what you have learned in 6202 and you will do great!",
														font = ('Tahoma', 20))
instructions.grid(column=1, row=0, padx=5, pady=5)




# Read the Image
image = Image.open("/Users/libbyellison/Desktop/6202 Game -  V1/books.jpg")
 
# Resize the image using resize() method
resize_image = image.resize((150,175))
 
img = ImageTk.PhotoImage(resize_image)
 
# create label and add resize image
label1 = Label(image=img)
label1.image = img

label1.grid(column=2, row=0, padx=5, pady=5)
  

label3 = tkinter.Label(root, text = "Type your name here \n then hit 'let's play!' to get started" ,
														font = ('Tahoma', 15))
label3.grid(column=0, row=1, padx=5, pady=5)


playername = tkinter.Entry(root,text = "Type your name here to begin.",font = ('Tahoma', 18))
playername.grid(column=0, row=2, padx=5, pady=5)
playername_value = playername.get()
print(playername_value)



login_button = tkinter.Button(root, text="Let's Play!", command=login_clicked)
login_button.grid(column=1, row=1, padx=5, pady=5)




# start the GUI
root.mainloop()
