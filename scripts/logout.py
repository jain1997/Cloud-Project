#!/usr/bin/python2
import commands
import os

print"content-type: text/html"
print 

#os.environ


logoutStatus=commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1}  iscsiadm --mode node --targetname {2} --portal 192.168.43.21:3260 --logout".format(passWord,ipAddress,username))

if logoutStatus[0]==0:
 print"Logout Successfully"
else:
 print"Failed To Logout"




