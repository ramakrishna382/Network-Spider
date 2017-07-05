import subprocess
import socket
import os
with open(os.devnull, "wb") as limbo:
        for n in xrange(10, 240):
                ip='10.4.16.{0}'.format(n)
                result=subprocess.Popen(["ping", "-n", "1", "-w", "200", ip],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print (ip, "inactive")
                else:
                        print (ip, "active")
