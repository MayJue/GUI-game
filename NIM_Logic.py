from tkinter import *


root = Tk()

def LeftTurn(event):
    print('left')

frame=Frame(root)
Button(frame, text="test", command= frame.focus).pack()
Entry(frame).pack()

frame.bind('<Enter>', LeftTurn)
frame.pack()

root.mainloop()