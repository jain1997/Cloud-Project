#!/usr/bin/python2


import cgi

print "content-type: text/html"

menuCh=cgi.FormContent()['setup'][0]

if menuCh == "staas":
	print "location: ../staasoption.html"
	print

elif menuCh == "docker":
	print "location: ../docker_index.html"
	print

elif menuCh == "iaas":
	print "location: ../iaas.html"
	print

elif menuCh == "pas":
	print "location: ../pas.html"
	print
elif menuCh == "saas":
        print "location: ../saas.html"
        print

else:
	print "not supported"













