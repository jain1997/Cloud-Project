#!/usr/bin/python2
print "Content-Type: text/html; charset=UTF-8"
print
import os 
import commands
import cgi
import getpass
"""
ipaddress=raw_input("enter ip")
osname=raw_input("enter osname")
username=raw_input("enter username")
password=getpass.getpass("enter password")
"""
ipaddress=cgi.FormContent()['ipaddress'][0]
osname=cgi.FormContent()['osname'][0]
username=cgi.FormContent()['username'][0]
password=cgi.FormContent()['password'][0]
#"""

runcontainer=" docker run -dit --name {0}-{1}{2} {1}:latest".format(username,osname,i)
sshpass="sudo sshpass -p {} ssh -o stricthostkeychecking=no -l root {}".format(password,ipaddress)
#running container 
containerrunstatus=commands.getstatusoutput("{0} {1}".format(sshpass,runcontainer))
if containerrunstatus[0]==0:
	print "Container ran successfully"
else:
	print "could not run "

