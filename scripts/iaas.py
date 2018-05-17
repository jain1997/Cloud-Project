#!/usr/bin/python2


import cgi
import commands
import os
print "content-type:  text/html"
print
print """
<script>
function ls1()
{
document.location='iaasmanage.py'
}

</script>
"""

osname=cgi.FormContent()['osname'][0]
ostype=cgi.FormContent()['ostype'][0]
cpunumber=cgi.FormContent()['cpunumber'][0]
storagesize=cgi.FormContent()['storagesize'][0]
ramsize=cgi.FormContent()['ramsize'][0]

cookie=os.environ['HTTP_COOKIE']

userName=cookie.split(",")[0].split("=")[1]
password=cookie.split(",")[1].split("=")[1]
ipaddress=cookie.split(",")[2].split("=")[1]
#print userName,password,ipaddress

#ilvcreate=commands.getstatusoutput("sudo lvcreate --size {0}G --name {1} myvg".format(storagesize,userName))
lvcreatestatus=commands.getstatusoutput("sudo lvcreate --size {} --name {} localvg".format(storagesize,userName))

if lvcreatestatus[0]==0:
	ossetup=commands.getstatusoutput("sudo virt-install --name  {0}  --location  /os/rhel-server-7.3-x86_64-dvd.iso  --os-type   linux  --os-variant  {1} --memory {2}   --vcpus  {3} --disk  /dev/localvg/{4},size={5} --graphics  vnc,password=redhat,listen=0.0.0.0,port=5901  --noautoconsole".format(osname,ostype,ramsize,cpunumber,userName,storagesize))

	#ssetupstatus=commands.getstatusoutput(ossetup)
	#print ssetupstatus
	
	if ossetup[0] == 0:
		print "<h2><center>os setup done</center></h2>"
	else:
		print "error"
else:
	print "no lv created"

print "<button onclick=ls1()>Manage your os</button>"
