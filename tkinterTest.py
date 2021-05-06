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

top.mainloop()
