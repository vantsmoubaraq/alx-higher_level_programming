#!/usr/bin/python3

from sys import argv

sum = 0

for i in range(len(argv)):
    if(i >= 1):
        sum += int(argv[i])

print("{:d}".format(sum))
