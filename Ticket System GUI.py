from tkinter import *

#Creating the class
class Ticket:
    def __init__(self, time, capacity, cost):
        self._time = time
        self._capacity = capacity
        self._cost = cost
        self._availability = capacity
        self._purchases = 0

        ticket.append(self)
        ticketNames.append(self._time)

    def _restore(self):
        self._availability = self._capacity


ticket = []
ticketNames = []

root = Tk()
root.title("Ticket Ordering System")
root.resizable(False, False)

#Default Tickets
Ticket("10AM", 150, 5)
Ticket("3PM", 150, 5)
Ticket("8PM", 250, 12)

#Default Variables
ticketType = StringVar()
ticketType.set("TICKETS")
numberTickets = IntVar()
soldTickets = 0
earnings = 0

#For adding new tickets
newName = StringVar()
newPrice = DoubleVar()
newPrice.set(0)
newCapacity = IntVar()

#For deleting tickets

toDelete = StringVar()
toDelete.set("TICKETS")

def create1():
    #Display Prices
    frame1 = Frame(root, relief = "groove", borderwidth = 2, width = 50)
    frame1.grid(row = 0, column = 0, sticky = N+S+W+E)

    Label(frame1, text = "CURRENT SHOWINGS").grid(row=0,column=0)
    rows = 1
    for i in ticket:
        if i._availability == 0:
            Label(frame1,text = "{} SHOW - {} available/{} capacity (${:.2f} each)".format(i._time, i._availability, i._capacity, i._cost), fg = "red").grid(row=rows, column = 0)
        else:
            Label(frame1,text = "{} SHOW - {} available/{} capacity (${:.2f} each)".format(i._time, i._availability, i._capacity, i._cost)).grid(row=rows, column = 0) 
        rows +=1
        
    return frame1

#Purchase Area
def create2():
    #Purchase Frame
    
    frame2 = Frame(root, relief = "groove", borderwidth = 2, width = 50)
    frame2.grid(row=0, column = 1, sticky = N+S+W+E)
    Label(frame2, text = "PURCHASE TICKETS").grid(row=0,column=0)
    Label(frame2, text ="TICKET: ").grid(row=1,column=0)
    OptionMenu(frame2, ticketType, *ticketNames).grid(row=1,column=1)
    
    Label(frame2, text = "NUMBER OF TICKETS: ").grid(row=2,column=0)
    Entry(frame2, textvariable = numberTickets).grid(row=2,column=1)

    Button(frame2, text = "SELL TICKETS", command = sell).grid(row=3, columnspan = 2)

    return frame2

#Function that runs upon clicking the button in Frame2. 
def sell():
    global frame1
    global frame2
    global frame3

    global ticketType
    global numberTickets

    global soldTickets
    global earnings
    
    try:
        for i in ticket:
            if i._time == ticketType.get():
                if (i._availability - numberTickets.get()) >= 0:
                    if numberTickets.get() <= 0:
                        messagebox.showwarning("Warning", "Please enter an integer greater than 0")
                    else:
                        i._availability -= numberTickets.get()
                        i._purchases += numberTickets.get()
                        soldTickets += numberTickets.get()
                        earnings += (i._cost * numberTickets.get())
                else:
                    messagebox.showwarning("Warning", "Not enough Tickets")

        
        frame1.destroy()
        frame1 = create1()

        frame2.destroy()
        frame2 = create2()

        frame3.destroy()
        frame3 = create3()
    except:
        messagebox.showwarning("Warning", "Please enter a valid integer")

#Summary
def create3():
    frame3 = Frame(root, relief = "groove", borderwidth = 2, width = 50)
    frame3.grid(row=1, column=0, sticky = N+E+W+S)

    Label(frame3, text = "SUMMARY").grid(row=0,column=0)
    Label(frame3, text = "{} tickets sold today".format(soldTickets)).grid(row=2,column=0)
    Label(frame3, text = "${:.2f} earned today".format(earnings)).grid(row=3,column=0)

    return frame3

#Reset Button
def create4():
    frame4 = Frame(root, relief = "groove", borderwidth = 2, width = 50)
    frame4.grid(row=2,column=1,sticky=N+W+E+S)

    Button(frame4, text = "RESET SHOWS", command = reset).grid(row=0,column=0, padx = 100)
    return frame4
    
def reset():
    global frame1
    global frame2
    global frame3
    global frame6

    global earnings
    global soldTickets
    global ticketType
    global numberTickets

    global newName
    global newCapacity
    global newPrice
    global toDelete

    earnings = 0
    soldTickets = 0
    ticketType.set("TICKETS")
    numberTickets.set(0)
    newName.set("")
    newCapacity.set(0)
    newPrice.set(0)
    toDelete.set("TICKETS")

    for i in ticket:
        i._restore()

    frame1.destroy()
    frame1 = create1()

    frame2.destroy()
    frame2 = create2()

    frame3.destroy()
    frame3 = create3()

    frame6.destroy()
    frame6 = create6()

#Adding new Tickets
def create5():
    frame5 = Frame(root, relief = "groove", borderwidth =2, width = 50)
    frame5.grid(row=2, column=0, sticky = N+S+W+E)

    Label(frame5, text = "ADD NEW TICKET TYPE").grid(column=0,row=0)
    Label(frame5, text = "NAME: ").grid(row=1,column=0)
    Label(frame5, text = "CAPACITY: ").grid(row=2,column=0)
    Label(frame5, text = "PRICE: ").grid(row=3,column=0)
    Entry(frame5, textvariable = newName).grid(row=1,column=1)
    Entry(frame5, textvariable = newCapacity).grid(row=2,column=1)
    Entry(frame5, textvariable = newPrice).grid(row=3,column=1)
    Button(frame5, text = "ADD TICKETS", command = addTicket).grid(row=4,column=0)
    return frame5

#Function that adds the tickets
def addTicket():
    global newName
    global newCapacity
    global newPrice

    global frame1
    global frame2
    global frame3
    global frame6
    try:
        duplicate = "NO"
        for i in ticket:
            if i._time == newName.get().upper():
                duplicate = "YES"
                break
        if duplicate == "NO":
            if newName.get().strip() != "":
                if newCapacity.get() > 0:
                    if newPrice.get() > 0:
                        Ticket(newName.get().upper(), newCapacity.get(), newPrice.get())
                        
                        frame1.destroy()
                        frame1 = create1()

                        frame2.destroy()
                        frame2 = create2()

                        frame3.destroy()
                        frame3 = create3()

                        frame6.destroy()
                        frame6 = create6()
                    else:
                        messagebox.showwarning("Warning", "Price must be greater than 0")
                else:
                    messagebox.showwarning("Warning", "Capacity must be greater than 0")
            else:
                messagebox.showwarning("Warning", "Ticket Name cannot be empty")
        else:
            messagebox.showwarning("Warning", "Ticket already exists")
    except:
        messagebox.showwarning("Warning", "Please enter valid inputs for Capacity and Price")

def create6():
    frame6 = Frame(root, relief = "groove", borderwidth = 2, width = 50)
    frame6.grid(row=1,column=1,sticky=N+S+W+E)

    Label(frame6, text= "DELETE TICKETS").grid(row=0,columnspan=2)
    Label(frame6, text = "TICKET: ").grid(row=2,column=0)
    OptionMenu(frame6, toDelete, *ticketNames).grid(row=2,column=1)
    Button(frame6, text = "DELETE", command = delete).grid(row=3,column=0)
    return frame6

def delete():
    global toDelete
    global frame1
    global frame2
    global frame3
    global frame6

    global soldTickets
    global earnings
    
    duplicate = "NO"
    for i in ticket:
        if i._time == toDelete.get():
            duplicate = "YES"
            break
    if duplicate == "YES":
        if len(ticket) > 1:
            if messagebox.askyesno("Warning", "Are you sure you want to delete this? All sales will be removed. "):
                for i in ticket:
                    if i._time == toDelete.get():
                        soldTickets -= i._purchases
                        earnings -= i._purchases*i._cost
                        ticket.remove(i)
                        ticketNames.remove(i._time)
                        toDelete.set("TICKETS")
                        break
                messagebox.showinfo("Success", "Ticket has been deleted")
                frame1.destroy
                frame1 = create1()

                frame2.destroy()
                frame2 = create2()

                frame3.destroy()
                frame3 = create3()

                frame6.destroy()
                frame6 = create6()
        else:
            messagebox.showwarning("Warning", "Cannot have no tickets available")
            
        
    

frame1 = create1()
frame2 = create2()
frame3 = create3()
frame4 = create4()
frame5 = create5()
frame6 = create6()

root.mainloop()
        
