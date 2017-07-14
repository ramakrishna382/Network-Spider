from Tkinter import *
import Tkinter as ttk
from ttk import *
import os ,socket ,subprocess

network = Tk(className ="Network")
network.geometry('1000x600') # Size 200, 200
network.resizable(width=False ,height=False)
svalue = StringVar() # defines the widget state as string
w = Entry(network ,width=80 ,textvariable=svalue) # adds a textarea widget
w.pack(side=TOP and LEFT)

w.place(x=3 ,y=3)
def act():

   ram = w.get()
   krishna = ARP_Scan(ram)
   text.insert("end", ARP_Scan(krishna) + "\n")
   text.see("end")


def lookup(addr):
    try:
        return socket.gethostbyaddr(addr)
    except socket.herror:
        return None, None, None


def ARP_Scan(ip_add_range):
    with open(os.devnull, "wb") as limbo:
        for n in xrange(1, 35):
            ip = ip_add_range.format(n)
            result = subprocess.Popen(["ping", "-n", "1", "-w", "200", ip],
                                      stdout=limbo, stderr=limbo).wait()
            if result:
               return ip + "inactive\n"
            else:
                name, alias, addresslist = lookup(ip)
                if name != None:
                    name1 = name
                    return ip + "\tactive\t" + name1

button1 = Button(network ,text="Press Me", command=act)
button1.pack()
# Add a grid
mainframe = Frame(network)
mainframe.grid(column=0 ,row=0, sticky=(N ,W ,E ,S))
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.place(x=10 ,y=30)

# Create a Tkinter variable
tkvar = StringVar(network)

# Dictionary with options
choices = { 'IP scanning' ,'openport scanning' ,'' ,'Finding Emails based on domainname' ,'OS footprinting'}
tkvar.set('Functionalities') # set the default option

popupMenu = OptionMenu(mainframe, tkvar, *choices)

popupMenu.grid(row =1, column =1)

# on change dropdown value
def change_dropdown(*args):
    print(tkvar.get())


# link function to change dropdown
tkvar.trace('w', change_dropdown)
text = Text(network, height=30, width=120)
text.grid(row=3, column=0)
text.insert(END, "I love my India\n")
vsb = Scrollbar( network,orient="vertical", command=text.yview)
text.configure(yscrollcommand=vsb.set)
vsb.pack(side="right", fill="y")
text.pack(side="left", fill="x", expand=True)
network.mainloop()

