This is a git post-receive that gives you (most of) the same data that you get
from github when you use its post-receive hook. The format we are trying to
duplicate is documented here: http://help.github.com/post-receive-hooks/

There are some differences - in particular, we provide nearly none of the
'repository' key information. Please set up the hook (see below) and dump the
output to see what you get.

Installation
------------
Start with ./setup.sh. You'll need virtualenv and the dev package for python installed (apt-get install
python-virtualenv python-dev for debian-based distros). This creates a virtualenv in this
directory.

Then, symlink your post-receive hook to uri-hook. NOT uri-hook.py.

(todo: a "call this script from your existing post-receive hook" mode)
