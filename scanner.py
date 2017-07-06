#import Tkinter

import subprocess
import socket
import os
#class simpleapp_tk(Tkinter.Tk):
 #   def __init__(self,parent):
  #      Tkinter.Tk.__init__(self,parent)
   #     self.parent = parent
    #    self.initialize()
    #def initialize(self):
     #   self.grid()
      #  self.entry = Tkinter.Entry(self)
       # self.entry.grid(column=0,row=0)





def lookup(addr):
     try:
         return socket.gethostbyaddr(addr)
     except socket.herror:
         return None, None, None
def ARP_Scan(ip_add_range):
    with open(os.devnull, "wb") as limbo:
        for n in xrange(1, 200):
                ip=ip_add_range.format(n)
                result=subprocess.Popen(["ping", "-n", "1", "-w", "200", ip],
                        stdout=limbo, stderr=limbo).wait()
                if  result:
                        print (ip, "inactive")
                else:

                        name,alias,addresslist = lookup(ip)
                        if name != None:
                            name1 = name
                            print (ip, "active",name1)



ARP_Scan("10.4.16.{0}")
#if __name__ =="__main__":
 #   app = simpleapp_tk(None)
  #  app.title('my application')
   # app.mainloop()
