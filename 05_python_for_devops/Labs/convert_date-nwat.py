#!/usr/bin/python3

import datetime
import sys
import argparse
    
if __name__ == "__main__":

    epoch = int(sys.stdin.read())
    parser = argparse.ArgumentParser(description= 'Convert current epoch time piped from bash')
    parser.add_argument('--iso', action='store_true', help= 'show as iso format')
    args = parser.parse_args()

    def convert_date():
        if args.iso is True:
            return datetime.datetime.fromtimestamp(epoch).isoformat()
        else:
            return datetime.datetime.fromtimestamp(epoch).strftime('%Y-%m-%d %I:%M %p')

    print(convert_date())