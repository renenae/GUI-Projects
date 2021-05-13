from tkinter import *
import random

top = Tk()
playlist = []
myRolls = []
dieType = 0
rollTimes = 0


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
    B1Main = Button(text= "Week 1", bg= "white", command = week1)
    B1Main.grid(column= 0, row = 2)
    B2Main = Button(text = "Week 2", bg= "white", command = week2)
    B2Main.grid(column= 0, row = 3)
    B3Main = Button(text = "Week 3", bg= "white")
    B3Main.grid(column= 0, row = 4)

def week1():
    clearWindow()
    def results():
        result = E1.get()
        playlist.append(result)
        E1.delete(0, END)
        
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

    B3 = Button(text = "Export List", bg = "yellow", command = exportList)
    B3.grid(column= 0, row= 3)

    Bexit = Button(text = "Main Menu", bg ="red", command = mainMenu)
    Bexit.grid(column= 1, row= 3)

def week2():
    def rollDice():
    #update variable data
        dieType = E2Week2.get()
        rollTimes = E1Week2.get()
        #clear the window AFTER updating variables
        clearWindow()
        #roll the dice
        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))

        #build results window 
        L4Week2 = Label()
        L5Week2 = Label()
        B2Week2 = Button()

        
    
    clearWindow()
    B1Week2 = Button(text= "Roll Em!", bg= "yellow")
    B1Week2.grid(column= 2, row= 4)

    L1Week2 = Label(top, text= "Dice roller app")
    L1Week2.grid(column= 2, row= 1)
    
    L2Week2 = Label(top, text= "# of Rolls")
    L2Week2.grid(column= 0, row= 2)
    
    L3Week2 = Label(top, text= "# of Sides")
    L3Week2.grid(column= 3, row= 2)
    
    E1Week2 = Entry(top, bd = 5)
    E1Week2.grid(column= 0, row= 3)
    
    E2Week2 = Entry(top, bd = 5)
    E2Week2.grid(column= 3, row= 3)







if __name__=="__main__":
    mainMenu()
    top.mainloop()

    
top.mainloop()
