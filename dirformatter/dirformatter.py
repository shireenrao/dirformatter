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
    # temp replace any %m to place holder  %1
    format = format.replace('%m','%1')
    # change m to place holder %2 which will be replaced with %m
    # and lstrip on 0 right before we produce the output
    format = format.replace('m','%2')
    # change back place holder %1 to %m
    format = format.replace('%1','%m')
    format = format.replace('dddd','%A')
    format = format.replace('ddd','%a')
    format = format.replace('dd','%d')
    # temp replace any %d to place holder %1
    format = format.replace('%d', '%1')
    # change d to placeholder %3 to be later replaced with lstrip %d
    format = format.replace('d','%3')
    # revert place holder back to %d
    format = format.replace('%1','%d')

    # begin special cases for singe d and singe m
    # replace %2 with real month without leading 0
    month_no_lead_zero = tstamp.strftime('%m').lstrip('0')
    format = format.replace('%2',month_no_lead_zero)
    # replace %3 with real day without leading 0
    day_no_leading_zero = tstamp.strftime('%d').lstrip('0')
    format = format.replace('%3',day_no_leading_zero)
    # end special cases

    formatted_str = tstamp.strftime(format)
    if formatted_str.find("/") > 0:
        tokens = formatted_str.split("/")
    elif formatted_str.find("\\") > 0:
        tokens = formatted_str.split("\\")
    else:
        tokens = formatted_str

    if target:
        destpath = os.path.join(target, *tokens)
    else:
        destpath = os.path.join(*tokens)

    return destpath

if __name__ == '__main__':
    if len(argv) == 1:
        format = 'yyyy/mmm/yyyy_mm_dd'
    else:
        format = argv[1]

    date_str = '2013-07-03 12:45:45'
    localtime = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    new_path = createdirpath(format, localtime, '/Users/shireenrao/mydev')
    print new_path
    new_path = createdirpath(format, localtime)
    print new_path



