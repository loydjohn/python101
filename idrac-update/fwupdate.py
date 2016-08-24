#!/usr/bin/python
import os
import commands
# Open a file - Input file for IDRAC Push
fo = open("idracip.txt", "r")
for ip in fo:
    ip = ip.strip()
    print ('Performing remote IDRAC Operations on -> %s' %ip)
    output = commands.getoutput("sshpass -p calvin ssh -o StrictHostKeyChecking=no root@%s 'racadm fwupdate -g -u -a 192.168.110.124'" % ip)
    fwupdate = open("%s" % ip, "w+")
    print output
    fwupdate.write(output)
    fwupdate.close()
# Close opend file
fo.close()