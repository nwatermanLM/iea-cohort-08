#!/usr/bin/env python

import datetime
import sys

epoch = int(sys.stdin.read())

print(datetime.datetime.fromtimestamp(epoch).strftime('%Y-%m-%d %H:%M:%S'))