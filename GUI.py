#Layout Management -
# 1. pack
# 2. place
# 3. grid

from tkinter import *

root = Tk()

def handleClick(btnVal):
    exp = strVar.get()
    if btnVal == "=":
        exp = str(eval(exp))
    elif btnVal == "X":
        exp = exp[:len(exp) - 1]
    elif btnVal == "CLEAR ALL":
        exp = ""
    else:
        exp += str(btnVal)
    strVar.set(exp)

strVar = StringVar()
strVar.set("")
Label(root, textvariable = strVar, width=40, height=5).grid(row=0, column = 0, columnspan=4)

Button(root, text="CLEAR ALL", command=lambda:handleClick("CLEAR ALL"), fg = "red", width=30, height=5).grid(row=1, column=0, columnspan=3)
Button(root, text="X", command=lambda:handleClick("X"), fg = "red", width=10, height=5).grid(row=1, column=3)

Button(root, text="7", command=lambda:handleClick("7"), width=10, height=5).grid(row=2, column=0)
Button(root, text="8", command=lambda:handleClick("8"), width=10, height=5).grid(row=2, column=1)
Button(root, text="9", command=lambda:handleClick("9"), width=10, height=5).grid(row=2, column=2)
Button(root, text="/", command=lambda:handleClick("/"), fg = "blue", width=10, height=5).grid(row=2, column=3)

Button(root, text="4", command=lambda:handleClick("4"), width=10, height=5).grid(row=3, column=0)
Button(root, text="5", command=lambda:handleClick("5"), width=10, height=5).grid(row=3, column=1)
Button(root, text="6", command=lambda:handleClick("6"), width=10, height=5).grid(row=3, column=2)
Button(root, text="*", command=lambda:handleClick("*"), fg = "blue", width=10, height=5).grid(row=3, column=3)

Button(root, text="1", command=lambda:handleClick("1"), width=10, height=5).grid(row=4, column=0)
Button(root, text="2", command=lambda:handleClick("2"), width=10, height=5).grid(row=4, column=1)
Button(root, text="3", command=lambda:handleClick("3"), width=10, height=5).grid(row=4, column=2)
Button(root, text="-", command=lambda:handleClick("-"), fg = "blue", width=10, height=5).grid(row=4, column=3)

Button(root, text=".", command=lambda:handleClick("."), fg = "green", width=10, height=5).grid(row=5, column=0)
Button(root, text="0", command=lambda:handleClick("0"), width=10, height=5).grid(row=5, column=1)
Button(root, text="=", command=lambda:handleClick("="), fg = "blue", width=10, height=5).grid(row=5, column=2)
Button(root, text="+", command=lambda:handleClick("+"), fg = "blue", width=10, height=5).grid(row=5, column=3)

root.mainloop()