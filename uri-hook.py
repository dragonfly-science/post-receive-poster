#!/usr/bin/env python

import argparse
import requests
import sys
from os import getcwd, stat, getuid
from os.path import basename
import pwd
import git
import json
from datetime import datetime

if __name__ == "__main__":
    repo = git.Repo(getcwd())

    try:
        destination = repo.config_reader().get_value('post-receive', 'url')
    except:
        sys.exit("Configure the URL to post to with git config post-receive.url [url]")

    parser = argparse.ArgumentParser()
    parser.add_argument('--oldrev', '-o')
    parser.add_argument('--newrev', '-n')
    parser.add_argument('--ref', '-r')
    args = parser.parse_args()

    if sys.stdin.isatty():
        raise Exception("Don't support running stand-alone (yet)")
    else:
        # Running in symlink mode
        (oldrev, newrev, ref) = sys.stdin.read().rstrip().split(' ')

    payload = {
        'after': newrev,
        'ref': ref,
        'before': oldrev,
        'repository': {
            'name': basename(repo.git_dir),
            'owner': {
                'name': pwd.getpwuid(stat(repo.git_dir).st_uid).pw_name,
            },
        },
        'pusher': {
            'name': pwd.getpwuid(getuid()).pw_name,
        },
        'commits': [],
    }

    for commit in repo.iter_commits('%s..%s' % (oldrev, newrev)):
        payload['commits'].append({
            'id': commit.hexsha,
            'removed': [],
            'added': [],
            'modified': [],
            'message': commit.message,
            'timestamp': datetime.fromtimestamp(commit.authored_date).strftime('%FT%T%z'),
            'author': {
                'name': commit.author.name,
                'email': commit.author.email,
            },
            'tmp': commit.stats.files
        })

    print json.dumps(payload, indent=4)
    requests.post(destination, data={'payload': json.dumps(payload)})
