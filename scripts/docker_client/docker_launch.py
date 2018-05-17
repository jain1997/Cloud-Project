#!/usr/bin/python2
import cgi
import commands
print "content-type: text/html"
print
#print cgi.FormContent()
#"""
imageName=cgi.FormContent()['imagename'][0]
cName=cgi.FormContent()['cname'][0]

if commands.getstatusoutput("sudo docker inspect {0}-{1}".format(cName,imageName.split(":")[0]))[0]==0:
#and (commands.getstatusoutput("sudo docker inspect {0} | jq '.[].Config.Image'".format(cName))[1].strip('"')==imageName):
	print "<b>{0}- {1}</b>:-Container of same name and OS image already exists ".format(cName,imageName)
	print "<button onclick=document.location='docker_run.py'>Previous Menu</button>"
else:
	runstatus=commands.getstatusoutput("sudo docker run -dit --name {0}-{2} {1}".format(cName,imageName,imageName.split(":")[0]))
	if runstatus[0]==0:
		print "<b>{0}:{1}</b>:-Conatainter launched...".format(cName,imageName.split(":")[0])
#		print "<a href='docker_manage.py'>Manage Conatainter</a>"
		print "<button onclick=document.location='docker_manage.py'>Manage</button> <button onclick=document.location='docker_index.py'>Main Menu</button>"

	else:
#		print runstatus
		print "could to run "
