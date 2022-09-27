#!/usr/bin/python3

import datetime
import sys
import argparse

epoch = int(sys.stdin.read())
local_conversion = datetime.datetime.fromtimestamp(epoch).strftime('%Y-%m-%d %H:%M:%S')
iso_conversion = datetime.datetime.utcfromtimestamp(epoch).isoformat()
parser = argparse.ArgumentParser(description= 'Convert current epoch time piped from bash')
parser.add_argument('--iso', action='store_true', help= 'show as iso format')
args = parser.parse_args()

if args.iso is True:
    print(iso_conversion)
else:
    print(local_conversion)

# def define_arguments()
# return parser

#def convert_date(epoch, args):
# return  datestring