#!/usr/bin/python2


import cgi

print "content-type: text/html"
#print "location: ../menu.html"


#print cgi.FormContent()

userName=cgi.FormContent()['username'][0]
passWord=cgi.FormContent()['password'][0]
ipaddress=cgi.FormContent()['ipaddress'][0]

d={0:'root',1:'redhat',2:'gaurav',3:'gauravjain'}

if userName == d[0] and passWord ==d[1] or userName == d[2] and passWord ==d[3]: 
#	print "<a href='../form.html'>click here to app</a>"
	print "set-cookie: username={0},password={1},ipaddress={2}".format(userName,passWord,ipaddress)
	print "location: ../menu.html"
	print

else:
	print "location: ../login.html"
	print




#print userName
#print passWord
