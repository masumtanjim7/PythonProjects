from cProfile import label
from tkinter import *
from tkinter.ttk import *

from time import strftime

root=Tk()
root.title("YouKnowWho's Clock")

def time():
    string = strftime("%I:%M:%S %p") #Here "%I"=12Hours if you want 24Hours then change it to "%H"
    label.config(text=string)
    label.after(1000,time)

label = Label(root, font=("ds-digital",100 ),background="black",foreground="cyan")
label.pack(anchor="center")
time()

mainloop()