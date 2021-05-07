from tkinter import *

top = Tk()
playlist = []

def results():
    result = E1.get()
    playlist.append(result)
    E1.delete(0, END)

def printList():
    print(playlist)

def exportList():
    with open('test.txt', 'w') as f:
        for item in playlist:
            f.write("%s/n" % item)



def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUI Projects")
    LMain.grid(column = 0, row = 1)
    B1Main = Button(text= "Week 1", bg= "white")
    B1.grid(column= 0, row = 2)
    B2Main = Button(text = "Week 2", bg= "white")
    B2.grid(column= 0, row = 3)
    B3Main = Button(text = "Week 3", bg= "white")
    B3.grid(column= 0, row = 4)

# This is a label widget
L1 = Label(top, text="Playlist Generator")
L1.grid(column= 0, row= 1)

# This is an Entry widget
E1 = Entry(top, bd = 5)
E1.grid(column= 0, row= 2)

# This is a Button widget 
B1 = Button(text= "  +  ", bg="yellow", command= results)
B1.grid(column= 1, row= 2)

B2 = Button(text= "  =  ", bg="cyan", command= printList)


B2.grid(column= 2, row= 2)

B3 = Button(text = "Export List", bg = "yellow", command= exportList)
B3.grid(column= 0, row= 3)

Bexit = Button(text = "Clear Window", bg ="red", command= clearWindow)
Bexit.grid(column= 1, row= 3)


top.mainloop()
