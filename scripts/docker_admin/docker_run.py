#!/usr/bin/python2
import docker_image_list
#print "<h1>welcome to Conatainter as a Service"
print "<h2>Lauch your Container:</h2>"
print "<form action='docker_launch.py'>"
print "Select your Image:"
docker_image_list.docker_list()
print """
<br/>
Enter your container name: <input name='cname'/>
<br/>
<input type ='submit'/>
</form>
<h2>Manage all the containers</h2><button onclick=document.location='docker_manage.py'>Manage</button>
"""
