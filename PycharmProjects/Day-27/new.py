import tkinter
from  tkinter import *

window=Tk()
window.title("Miles to Kms")
window.config(padx=50,pady=50)
# window.minsize(500,200)

def clicked ():
    km=round(float(input.get())*1.609,2)
    text_4 = Label(text=f"{km}")
    text_4.grid(row=3, column=3)


text_1=Message(text="Mile(s)")
text_1.grid(row=2,column=4)


text_2=Label(text="is equal to")
text_2.grid(row=3,column=2)


text_3=Label(text="Km(s)")
text_3.grid(row=3,column=4)


input=Entry(width=7)
input.grid(row=2,column=3)
input.config()
input.get()

button=Button(text="miles",command=clicked)
button.config(text="Calculate")
button.grid(row=4,column=3)



tkinter.mainloop()