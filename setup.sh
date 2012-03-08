#!/bin/sh
[ -e bin/activate ] || virtualenv -p python2.7 --no-site-packages .
pip install GitPython
pip install requests
