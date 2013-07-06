#!/usr/bin/env python
'''
This module takes a date object and a format string and will create a directory
structure based on that format string

Default structure created under target directory
is yyyy/mmmm/yyyy_mm_dd
e.g. 2013/January/2013_01_13
The format is supplied as "yyyy/yyyy_mm_dd".
This will create a directory structure of the format
"2013/2013_01_13" under your target directory.
Where 2013 is a sub-directory under the target
directory and 2013_01_13 is a sub-directory under
2013

Here are the possible format types -
d    day as a number without leading zero (1-31)
dd   day as a number with leading zero (01-31)
ddd  day as an abreviation (Sun-Sat)
dddd day as a full name (Sunday-Saturday)
m    month as a number without leading zero (1-12)
mm   month as a number with leading zero (01-12)
mmm  month as an abreviation (Jan-Dec)
mmmm month as a full name (January-December)
yy   year as a two-digit number (00-99)
yyyy year as a four digit number
'''
#import time
from datetime import datetime
import os
from sys import argv

def createdirpath(format, tstamp, target=None):
    format = format.replace('yyyy','%Y')
    format = format.replace('yy','%y')
    format = format.replace('mmmm','%B')
    format = format.replace('mmm','%b')
    format = format.replace('mm','%m')
    format = format.replace('dddd','%A')
    format = format.replace('ddd','%a')
    format = format.replace('dd','%d')

    formatted_str = tstamp.strftime(format)
    tokens = formatted_str.split("/")

    destpath = os.path.join(*tokens)
    return destpath

if __name__ == '__main__':
    if len(argv) == 1:
        format = 'yyyy/mmm/yyyy_mm_dd'
    else:
        format = argv[1]

    date_str = '2013-07-03 12:45:45'
    localtime = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    new_path = createdirpath(format, localtime)
    print new_path


