#from tkinter import *
import os
from Control import Bin2Decimal

prueba = Bin2Decimal.Conversor()
prueba.n = 1000591038
prueba.decimalToBinary()

"""""
root = Tk()
root.title("Conversor de bases numericas")
root.geometry('350x200')

lbl = Label(root, text="Este es mi año Henderson!")
lbl.grid()

txt = Entry(root, width=10)
txt.grid(column=1, row=0)


def clicked():
    res = "You wrote " + txt.get()
    lbl.configure(text=res)


btn = Button(root, text="Click me", fg="red", command=clicked)
btn.grid(column=2, row=0)

root.mainloop()
"""