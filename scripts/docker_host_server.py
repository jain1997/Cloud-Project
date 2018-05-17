#!/usr/bin/python2
import docker_image_list
#print "content-type: text/html \n"
print"""
<!DOCTYPE html>
<html>
<head>
  <title>
    Host Personal Server
  </title>
</head>
<script>
</script>
<body>
  <h1 align="center">Host Personal Server</h1>
      <div align="center">
        <form action="docker_server_setup.py">
"""
print "Select your Image:"
docker_image_list.docker_list()
print """
        SSH Server<input type="radio" name="ssh"/>
        Apache server<input type="radio" name="httpd"/>
        <input type="submit" value="submit"/>
        <p>(Chose Any One)</p>
      </form>
      </div>
</body>
</html>
"""
