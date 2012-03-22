#!/bin/bash
[ -e bin/activate ] || virtualenv -p python2.7 --no-site-packages .
. bin/activate
pip install GitPython
pip install requests
