#!/bin/bash
[ -e bin/activate ] || virtualenv -p python --no-site-packages .
. bin/activate
pip install GitPython
pip install requests
pip install argparse
