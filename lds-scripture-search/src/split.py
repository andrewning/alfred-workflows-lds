#!/usr/bin/env python
# encoding: utf-8
"""
split.py

Created by Andrew Ning on 2013-04-28.
"""

import sys

# get query from user
query = sys.argv[1]
action = sys.argv[2]

parts = query.split('***')

if action == 'copy':
    sys.stdout.write(parts[0])

elif action == 'url':

    from subprocess import call
    call(['open', parts[1]])
