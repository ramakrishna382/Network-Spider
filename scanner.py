from Tkinter import *
import Tkinter as ttk
from ttk import *
import os ,socket ,subprocess,threading,Queue
from tkFileDialog import *
from punter import search


network = Tk(className ="Network")
network.geometry('1000x600') # Size 200, 200
network.resizable(width=False ,height=False)
svalue = StringVar() # defines the widget state as string
w = Entry(network ,width=80 ,textvariable=svalue) # adds a textarea widget
w.pack(side=TOP and LEFT)
w.place(x=3 ,y=3)



common_ports = {

    "7   ": "Echo",
    "19  ":"chargen",
    "21  ": "ftp",
    "22  ": "ssh",
    "23  ": "Telnet",
    "25  ": "smtp",
    "43  ": "whois",
    "53  ": "DNS",
    "69  ": "TFTP",
    "70  ": "Gopher",
    "79  ": "Finger",
    "80  ": "http",
    "110 ": "POP3",
    "113 ": "Ident",
    "119 ": "NNTP",
    "123 ": "NTP",
    "143 ": "IMAP4",
    "177 ": "xdmcp",
    "179 ": "bgp",
    "201 ": "AppleTalk",
    "269 ": "BGMP",
    "318 ": "TSP",
    "389 ": "LDAP",
    "443 ": "https",
    "464 ": "Kerberos",
    "497 ": "Retrospect",
    "512 ": "Rexec",
    "513 ": "rlogin",
    "514 ": "syslog",
    "520 ": "RIP",
    "540 ": "UUCP",
    "554 ": "RTSP",
    "560 ": "Rmonitor",
    "639 ": "MSDP",
    "902 ": "VMS",
    "1026": "WM"

}

def open1():
    file = askopenfile(mode='r', defaultextension=".txt")
    if file is None:
        return
    text.insert(END, file.read())

def file_save():
    f = asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(text.get(1.0, END)) # starts from `1.0`, not `0.0`
    f.write(text2save)
    f.close() # `()` was missing.

def clear_text():
    text.delete(1.0, END)

def lookup(addr):
    try:
        return socket.gethostbyaddr(addr)
    except socket.herror:
        return None, None, None

def act():
    ram = w.get()
    clear_text()
   # if(ram ! ):
    #    showerror("enter range of ip address")
    ARP_Scan(ram)

def act1():
    ram = w.get()
    clear_text()
    p_scan(ram)

def act2():
    hack = w.get()
    clear_text()
    email(hack)

def create_window():
    window =Toplevel(network)
    window.focus_set()
    window.label = StringVar()
    window.label.set("""
            NetworkSpider is a Python network analyzing application.\n
            We are having 7 buttons and one entry in this application.\n
            First of all you need to select which functionality you want .\n
            after that you can give your input in the entry field.\n
            then you can click the highlighted search button .\n
            then you will see the desired output in a text box below.\n
            SAVE:\tthis button stores output in a text box in a file for future references.\n
            LOAD:\twe can see the files that we stored for future references in a text box in our application.\n
            HELP:\tthis button describe how to use our application.\n
            ABOUT:\tabout our team.""")
    window.labe1 = Label(window, textvariable=window.label)
    window.labe1.pack()
def create_window2():
    window =Toplevel(network)
    window.focus_set()
    window.label1 = StringVar()
    window.label1.set(""" Our team contains three members\n
                RamaKrishna\n
                Ganapathi\n
                SwarnaLatha.\n
      """)
    window.labe2 = Label(window, textvariable=window.label1)
    window.labe2.pack()
def email(domain):
    text.insert(END,"Wait. Process is running........\n")

    # Exception hadling
    try:
        email_search = search("af594dea520ae66443724868f4a3e62dd24a8fb4", domain,
                              type='personal')  # Trying to retrieve Personal Email IDs
        email_list = email_search['emails']  # it is a list type variable  (type(email_list))
        personal_emails = []
        for email in email_list:
            personal_emails.append(email['value'])

    except:
        personal_emails = []
        text.insert(END,"No Email IDs were found...\n")  # If no records retrieved
    try:
        email_search = search("af594dea520ae66443724868f4a3e62dd24a8fb4", domain,
                              type="generic")  # Trying to retrieve Generic Email IDs
        email_list = email_search['emails']
        generic_emails = []
        for email in email_list:
            generic_emails.append(email['value'])
    except:
        generic_emails = []
        text.insert(END,"No Email IDs were found...\n")  # If no records retrieved

        # Printing the results
    text.insert(END,"Personal Email IDs....==\n")

    for ids in personal_emails:
        text.insert(END,ids + "\n")

    text.insert(END,"\nGeneric Email IDs....\n==")

    for ids in generic_emails:
        text.insert(END,ids + "\n")


def ARP_Scan(ip_add_range):
    with open(os.devnull, "wb") as limbo:
        text.insert(END,"IP ADDRESS\t\tSTATE\t\tHOST NAME\n\n","big")
        x=0
        for n in xrange(1, 255):
            ip = ip_add_range.format(n)
            result = subprocess.Popen(["ping", "-n", "1", "-w", "200", ip],
                                      stdout=limbo, stderr=limbo).wait()
            if result:
               #text.insert(END,ip + "\t\tinactive\n")
                y=0
            else:
                name, alias, addresslist = lookup(ip)
                if name != None:
                    name1 = name
                    x = x + 1
                    text.insert(END,ip + "\t\tactive\t\t" + name1+"\n")

    if x==0:
        text.insert(END,"No IP's are active in this range")

def is_port_open(host, port):
    try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        sock.connect((host, port))
    except socket.error:
        return False
    return True


def scan(host):
    clear_text()
    text.insert(END, "Number\t\tPORT_NAME\t\t\tState\n\n")
    while True:

        port = port_queue.get()
        if is_port_open(host, port):

            if str(port) in common_ports:
                first = str('{}\t\t({})\t\t\tOpen'.format(str(port), common_ports[str(port)]))
                text.insert(END,str(first) + "\n")
            else:
                second = str('{}\t\t\t\t\tOpen'.format(port))
                text.insert(END,str(second) + "\n")
        port_queue.task_done()


port_queue = Queue.Queue()
def p_scan(ram):

    for _ in range(20):
        t = threading.Thread(target=scan, kwargs={"host": ram})
        t.daemon = True
        t.start()
    for port in range(30000):
        port_queue.put(port)

port_queue.join()
# Add a grid
mainframe = Frame(network)
mainframe.grid(column=0 ,row=0, sticky=(N ,W ,E ,S))
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.place(x=10 ,y=30)

# Create a Tkinter variable
tkvar = StringVar(network)

# Dictionary with options
choices = { 'IP scanning' ,'openport scanning' ,'' ,'Finding Emails based on domainname' }
tkvar.set('Functionalities') # set the default option

popupMenu = OptionMenu(mainframe, tkvar, *choices)

popupMenu.grid(row =1, column =1)
# on change dropdown value
def change_dropdown(*args):
    if(tkvar.get() == "IP scanning"):
        button1.state(["!disabled"])
        button2.state(["disabled"])
        button3.state(["disabled"])
    elif(tkvar.get() == "openport scanning"):
        button2.state(["!disabled"])
        button3.state(["disabled"])
        button1.state(["disabled"])
    elif(tkvar.get() == "Finding Emails based on domainname"):
        button3.state(["!disabled"])
        button2.state(["disabled"])
        button1.state(["disabled"])
    else:
        button1.state(["disabled"])
        button2.state(["disabled"])
        button3.state(["disabled"])



button1 = Button(network, text="Search", command=act)
button1.state(["disabled"])
button1.pack()

button2 = Button(network, text="Search", command=act1)
button2.state(["disabled"])
button2.pack()

button3 = Button(network, text="Search",command=act2)
button3.state(["disabled"])
button3.pack()

button4 = Button(network, text="Load",command=open1)
button4.place(x=546)
button5 = Button(network, text="Save",command=file_save)
button5.place(x=546,y=25)
button6 = Button(network, text="HELP",command=create_window)
button6.place(x=630)
button7 = Button(network, text="ABOUT",command=create_window2)
button7.place(x=630,y=25)
# link function to change dropdown
tkvar.trace('w', change_dropdown)
text = Text(network, height=30, width=120)
text.grid(row=3, column=0)
vsb = Scrollbar( network,orient="vertical", command=text.yview)
text.configure(yscrollcommand=vsb.set)
vsb.pack(side="right", fill="y")
text.pack(side="left", fill="x", expand=True)
network.mainloop()

