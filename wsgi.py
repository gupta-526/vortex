#!/usr/bin/env python
import os
import imp
import sys

try:
  pyenv = os.environ.get('PYENV')
  python_version = "python"+str(sys.version_info[0])+"."+str(sys.version_info[1]) 
  # os.environ['PYTHON_EGG_CACHE'] = os.path.join(pyenv, 'lib', python_version, 'site-packages')
    
except IOError:
  pass
#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

from run import flask_app as application

# Below for testing only
#

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 5000, application)
    # Wait for a single request, serve it and quit.
    httpd.serve_forever()
