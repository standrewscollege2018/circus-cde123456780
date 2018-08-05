from tkinter import *

#Creating the class
class Ticket:
    def __init__(self, time, capacity, cost):
        self._time = time
        self._capacity = capacity
        self._cost = cost
        self._available = capacity

        ticket.append(self)
        ticketNames.append(self._time)


ticket = []
ticketNames = []

root = Tk()
root.title("Ticket Ordering System")

#Default Tickets
Ticket("10AM", 150, 5)
Ticket("3PM", 150, 5)
Ticket("8PM", 250, 12)

#Default Variables
ticketType = StringVar()
ticketType.set("TIME")
numberTickets = IntVar()


def create1():
    #Display Prices
    frame1 = Frame(root, relief = "groove", borderwidth = 2, width = 50)
    frame1.grid(row = 0, column = 0, sticky = N+S+W+E)

    Label(frame1, text = "CURRENT SHOWINGS").grid(row=0,column=0)
    rows = 1
    for i in ticket:
        Label(frame1,text = "{} SHOW - {} available/{} capacity (${} each)".format(i._time, i._available, i._capacity, i._cost)).grid(row=rows, column = 0) 
        rows +=1
        
    return frame1

def create2():
    #Purchase Frame
    frame2 = Frame(root, relief = "groove", borderwidth = 2, width = 50)
    frame2.grid(row=0, column = 1, sticky = N+S+W+E)
    Label(frame2, text = "PURCHASE TICKETS").grid(row=0,column=0)
    OptionMenu(frame2, ticketType, *ticketNames).grid(row=1,column=0)

    Label(frame2, text = "NUMBER OF TICKETS: ").grid(row=2,column=0)
    Entry(frame2, textvariable = numberTickets).grid(row=2,column=1)

    Button(frame2, text = "SELL TICKETS", command = sell).grid(row=3, columnspan = 2)

    return frame2

def sell():
    global frame1
    global frame2

    global ticketType
    global numberTickets

    for i in ticket:
        if i._time == ticketType:
            if (i._availability - numberTickets.get()) >= 0:
                i._availability -= (numberTickets.get())
            else:
                messagebox.showinfo("Warning", "Not enough Tickets")

    frame1.destroy()
    frame1 = create1()

    frame2.destroy()
    frame2 = create2()

    


frame1 =create1()
frame2 = create2()

        
