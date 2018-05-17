#!/usr/bin/python2
import commands
import cgi


print"content-type: text/html"
print

#Step1 Make a Partition

#We are Now going to create a LV
#ipAddress=raw_input("Enter IP Addres")
#passWord=getpass.getpass("Enter Password of root Account")
ipAddress=cgi.FormContent()['ip'][0]
passWord=cgi.FormContent()['pass'][0]
lvSize=cgi.FormContent()['size'][0]
userName=cgi.FormContent()['user'][0]


vgStatusOutput=commands.getstatusoutput("sudo vgdisplay  localvg")
if vgStatusOutput[0]==0:
  print"<b> Volume group Found<b>"
else:
  print "<b>Volume Group Not Find<b>"
  exit()



lvStatus=commands.getstatusoutput("sudo lvcreate  --size {0}G  --name  {1}-lv1    localvg".format(lvSize,userName))
if lvStatus[0]==0:
 print"lvcreated successfully" 
else:
 print"lvnotcreated Try Again!!"

#Formatting the Drive
#Step2 
formatStatus=commands.getstatusoutput("sudo  mkfs.ext4  /dev/localvg/{0}-lv1".format(userName))
if formatStatus[0]==0:
 print"Drive Formatted"
else:
 print"Drive Not Formatted"

#Mounting 
#Step3

folderStatus=commands.getstatusoutput(" sudo mkdir  -p  /share/{0}".format(userName))

if folderStatus[0]==0:
 print"Folder Created"
else:
 print"Folder Not Created"

mountStatus=commands.getstatusoutput("sudo mount /dev/localvg/{0}-lv1  /share/{0}".format(userName))
if mountStatus[0]==0:
 print"Mounting Done"
else:
 print"Mounting Unsuccessfull"

commands.getoutput("chown apache /etc/exports")
fileStatus=commands.getstatusoutput("sudo echo '/share/{}  *(rw,no_root_squash)' >>  /etc/exports".format(userName))

if fileStatus[0]==0:
 print"File Writted"
else:
 print"File Not Writted"

nfsServiceStatus=commands.getstatusoutput("sudo systemctl restart nfs")
if nfsServiceStatus[0]==0:
 print"NFS Service Started"
else:
 print"NFS Service Failed"

mountPoint=commands.getstatusoutput("sudo sshpass -p  {0}  ssh  -o stricthostkeychecking=no  -l  root  {2}  mkdir    /media/{1} " .format(passWord,userName,ipAddress))

if mountPoint[0]==0:
 print"Mount Point Created"
else:
 print"Mount Point Not Created"

driveStatus=commands.getstatusoutput("sudo sshpass -p  {0}  ssh  -o stricthostkeychecking=no -l root  {2}  mount  192.168.43.137:/share/{1}   /media/{1}".format(passWord,userName,ipAddress))

if driveStatus[0]==0:
 print "Drive Sucessfully Created"
else:
 print" Drive Not Created"



# For Peramanent Mounting
#/etcfstab
#step4
#NFS SERVER CONFIGURATION
#contentWrite=commands.getoutput("/share/  allowedip ")
#f=open('/etc/exports','a') 
#f.write(contentWrite+"\n")
#f.close()


