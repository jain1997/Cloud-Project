#!/usr/bin/python2


import cgi

print "content-type: text/html"

menuCh=cgi.FormContent()['setup'][0]

if menuCh == "staas":
	print "location: ../staasobject.html"
	print

elif menuCh == "staasblock":
        print "location: ../staasblock.html"
        print

else:
	print "not supported"













