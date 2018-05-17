#!/usr/bin/python2
import commands
import cgi 

print"content-type: text/html" 
print

ipAddress=cgi.FormContent()['ipaddress'][0]
passWord= cgi.FormContent()['password'][0]
size=cgi.FormContent()['size'][0]
username=cgi.FormContent()['name'][0]


#step 1: Install ISCSI Server on TARGET

#commands.getstatusoutput("ansible-playbook  scsi.yml")


#step 2: Configure ISCSI Server(created LV)

lvStatus=commands.getstatusoutput("sudo lvcreate  --size {0}G   --name {1}  localvg".format(size,username))

if lvStatus[0]==0:
 print "lv Created"
else:
 print "lvnot Created"

#Step 3: Run the Server
serviceStatus= commands.getstatusoutput("sudo systemctl restart tgtd")
if serviceStatus[0]==0:
 print"Service Started"
else:
 print"Service Failed"

#Step4 
#Giving Permissions to apache folder

commands.getoutput("sudo chown apache  /etc/tgt/targets.conf")

str="<target {0}>\n backing-store /dev/localvg/{0} \n</target>".format(username)
f=open("/etc/tgt/targets.conf",'a')
f.write(str+"\n")
f.close()
commands.getoutput("sudo sshpass -p {} ssh -o stricthostkeychecking=no  -l root   {} systemctl restart tgtd".format(passWord,ipAddress))
commands.getoutput("sudo systemctl restart tgtd")
#Step 4 Install ISCSI init on Client

#Step5 	Service Status Client Side!!

discoverStatus=commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} iscsiadm --mode discoverydb --type sendtargets --portal 192.168.43.137 --discover".format(passWord,ipAddress))

if discoverStatus[0]==0:
 print" Target Found"
else:
 print"Target Not Found"


loginStatus=commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} iscsiadm --mode node --targetname  {2} --portal 192.168.43.137:3260 --login".format(passWord,ipAddress,username))


if loginStatus[0]==0:
 print"Login Successfully"
else:
 print "Failed to Login"


print "<a href='logout.py'> Click Here To logout</a>"
#print "<a href='lvextend.py'>Click here to extend the size</a>"



