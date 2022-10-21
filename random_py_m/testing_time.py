#!/usr/bin/env python3

import datetime as DT

def get_datetime():
    timenow = DT.datetime.now()
    date = timenow.date().isoformat()
    time = timenow.time().isoformat(timespec='seconds')
    time_format = timenow.strftime('%I:%M %p')
    date_format = timenow.strftime('%B %d, %Y')
    return date, time, time_format, date_format

if __name__=="__main__":
    print(get_datetime())
