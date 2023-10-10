from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Springarvandring")
root.geometry("1000x800+0+0")
root.resizable(0,0)
#root.rowconfigure(0, weight=1)
#root.columnconfigure(0, weight=1)

leftframe = Frame(root,highlightbackground="black",highlightthickness=2)
leftframe.pack(side="left")

knight = PhotoImage(file="yes.png")
"""
boardframe = Frame(leftframe,highlightbackground="blue",highlightthickness=2)
boardframe.pack(side="top")

for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            label = Label(boardframe, height=4, width=7, bg="#695307")
            label.grid(column=i,row=j)
        else:
            label = Label(boardframe, height=4, width=7, bg="#A95307")
            label.grid(column=i,row=j)
"""

boardcanvas = Canvas(leftframe,highlightbackground="blue",highlightthickness=2,width=600,height=600)
boardcanvas.pack()

for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            boardcanvas.create_rectangle(75*i,75*j,75*(i+1),75*(j+1),fill="#edce93")
        else:
            boardcanvas.create_rectangle(75*i,75*j,75*(i+1),75*(j+1),fill="#a8720a")

bottomframe = Frame(leftframe,highlightbackground="blue",highlightthickness=2)
bottomframe.pack(side="bottom")
prevMoveButton = Button(bottomframe, text="<-").pack(side="left")
nextMoveButton = Button(bottomframe, text="->").pack(side="left")

menuframe = Frame(root,highlightbackground="blue",highlightthickness=2)
menuframe.pack(side="left")

randomWalkButton = Button(menuframe, text="Generera slumpad vandring")
inputWalkButton = Button(menuframe, text="Skriv in din egen vandring")
completeWalkButton = Button(menuframe, text="Besök alla rutor")
randomWalkButton.pack()
inputWalkButton.pack()
completeWalkButton.pack()


label = Label(menuframe, text="fuck you")
label.pack()



#ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1,row=0)


root.mainloop()

