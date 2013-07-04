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
import time
from sys import argv

localtime = time.localtime(time.time())
#print "Local current time :", localtime
#print time.strftime("%a", localtime)
format = argv[1]
print format
tokens = format.split("/")
print tokens
tokens = [token.replace('yyyy',time.strftime("%Y", localtime)) for token in tokens]
tokens = [token.replace('yy',time.strftime("%y", localtime)) for token in tokens]
tokens = [token.replace('mmmm',time.strftime("%B", localtime)) for token in tokens]
tokens = [token.replace('mmm',time.strftime("%b", localtime)) for token in tokens]
tokens = [token.replace('mm',time.strftime("%m", localtime)) for token in tokens]
#tokens = [token.replace('m',time.strftime("%m", localtime)) for token in tokens]
tokens = [token.replace('dddd',time.strftime("%A", localtime)) for token in tokens]
tokens = [token.replace('ddd',time.strftime("%a", localtime)) for token in tokens]
tokens = [token.replace('dd',time.strftime("%d", localtime)) for token in tokens]
tokens = [token.replace('d',time.strftime("%e", localtime)) for token in tokens]

print tokens

