#!/usr/bin/python2
import commands
print "content-type: text/html"
print
print """
<head><title>Manage All Dockers</title></head>
<script>
function stop(mycname)
{
document.location='docker_stop.py?x=' + mycname;
}
function start(mycname)
{
document.location='docker_start.py?x=' + mycname;
}

function remove(mycname)
{
document.location='docker_remove.py?x=' + mycname;
}
</script>
"""
print "<table border='3'>"
print "<tr><th>Image Name</th><th>Container Name</th><th>Ip Address</th><th>Status</th><th>stop</th><th>Start</th><th>Remove</th></tr>"
z=1
for i in commands.getoutput("sudo docker ps -a").split('\n'):
    if z==1:
        z+=1
        pass
    else:
        j=i.split()
        cStatus=commands.getoutput("sudo docker inspect {0} | jq '.[].State.Status'".format(j[-1]))
        cIpAddress=commands.getoutput("sudo docker inspect {0} | jq '.[].NetworkSettings.IPAddress'".format(j[-1]))
        print "<tr><td>" + j[1]+"</td><td>" + j[-1]+"</td><td>"+cIpAddress.strip('\"')  +"</td><td>"+cStatus.strip('\"')+"</td><td><input value='" + j[-1] + "' type='button' onclick=stop(this.value)  /></td><td><input value='" + j[-1] + "' type='button' onclick=start(this.value)  /></td><td><input value='" + j[-1] + "' type='button' onclick=remove(this.value)  /></td></tr>"
print "</table>"
