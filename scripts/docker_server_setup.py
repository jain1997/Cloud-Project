#!/usr/bin/python2
import cgi
print "content-type: text/html\n"
imageName=cgi.FormContent('imagename')[0]
if cgi.FormContent()['ssh'][0]=="on":
    
