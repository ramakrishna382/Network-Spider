from Tkinter import *
import Tkinter as ttk
from ttk import *
import os ,socket ,subprocess,threading,Queue

network = Tk(className ="Network")
network.geometry('1000x600') # Size 200, 200
network.resizable(width=False ,height=False)
svalue = StringVar() # defines the widget state as string
w = Entry(network ,width=80 ,textvariable=svalue) # adds a textarea widget
w.pack(side=TOP and LEFT)

w.place(x=3 ,y=3)

common_ports = {

    "7": "Echo",
    "21": "ftp",
    "22": "ssh",
    "23": "Telnet",
    "25": "smtp",
    "53": "DNS",
    "79": "Finger",
    "80": "http",
    "110": "POP3",
    "143": "IMAP4",
    "201": "AppleTalk",
    "443": "https",
    "520": "RIP",
    "902": "VMS",
    "1026": "WM"
}

def lookup(addr):
    try:
        return socket.gethostbyaddr(addr)
    except socket.herror:
        return None, None, None

def act():
    ram = w.get()
    ARP_Scan(ram)
    scan(ram)



def ARP_Scan(ip_add_range):
    with open(os.devnull, "wb") as limbo:
        for n in xrange(1, 35):
            ip = ip_add_range.format(n)
            result = subprocess.Popen(["ping", "-n", "1", "-w", "200", ip],
                                      stdout=limbo, stderr=limbo).wait()
            if result:
               text.insert(END,ip + "\t\tinactive\n")
            else:
                name, alias, addresslist = lookup(ip)
                if name != None:
                    name1 = name
                    text.insert(END,ip + "\t\tactive\t\t" + name1+"\n")



def is_port_open(host, port):
    try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        sock.connect((host, port))
    except socket.error:
        return False
    return True


def scan(host):
    while True:
        port = port_queue.get()
        if is_port_open(host, port):
            if str(port) in common_ports:
                first = str("{}\t\t({})\t\t\tOpen".format(str(port), common_ports[str(port)]))
                text.insert(END,str(first))
            else:
                second = str("{}\t\t\t\t\tOpen".format(port))
                text.insert(END,str(second))
        port_queue.task_done()


port_queue = Queue.Queue()
host = w.get()
for _ in range(20):
    t = threading.Thread(target=scan, kwargs={"host": host})
    t.daemon = True
    t.start()
for port in range(30000):
    port_queue.put(port)

port_queue.join()





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
vsb = Scrollbar( network,orient="vertical", command=text.yview)
text.configure(yscrollcommand=vsb.set)
vsb.pack(side="right", fill="y")
text.pack(side="left", fill="x", expand=True)
network.mainloop()

