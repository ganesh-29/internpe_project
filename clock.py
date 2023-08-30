from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title("digital clock")
def ram():
    sai=strftime("%H:%M:%S %p")
    label.config(text=sai)
    label.after(1000,ram)
label=Label(root,font=("aerial",90,"underline"),foreground="red",background="green")
label.pack(anchor="center")
ram()
mainloop()
