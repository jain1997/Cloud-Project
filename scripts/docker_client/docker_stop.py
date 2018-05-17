#!/usr/bin/python2
import commands
import cgi
print "content-type: text/html"
#print
cName=cgi.FormContent()['x'][0]
#print cgi.FormContent()['x'][0]

cstopstatus=commands.getstatusoutput("sudo docker stop {}".format(cName))

if cstopstatus[0]==0:
    print "location: docker_manage.py"
    print

else:
    print "not stopped"
#"""
