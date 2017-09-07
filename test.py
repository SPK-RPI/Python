from tkinter import *
import tkinter.messagebox
root=Tk()
canvas = Canvas(root,width=500,height=600)
canvas.pack()


def action():
    canvas.create_rectangle(25 ,25 ,130 ,60,fill='red')

def action1():
    canvas.create_rectangle(25 ,25 ,130 ,60,fill='green')

def action2():
     canvas.create_rectangle(25 ,25 ,1002 ,60,fill='gray')
def action3():
     canvas.create_rectangle(25 ,25 ,130 ,623,fill='purple')
def action4():
     canvas.create_rectangle(25 ,25 ,130 ,60,fill='yellow')


topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
button1 = Button(topFrame,text="boton 1",bg="red",command=action)
button2 = Button(topFrame,text="boton 2",bg="green",command=action1)
button3 = Button(topFrame,text="boton 3",bg="gray",command=action2)
button4 = Button(topFrame,text="boton 4",bg="purple",command=action3)
button5 = Button(topFrame,text="boton 5",bg="yellow",command=action4)

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
button5.pack(side=LEFT)


root.mainloop()