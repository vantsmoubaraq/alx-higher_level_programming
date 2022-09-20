#!/usr/bin/python3

for letter in range(ord('z'),ord('a')-1,-1):
    if(letter % 2 == 0):
        print(f"{chr(letter)}",end = '')
    else:
        print(f"{chr(letter -(ord('a') - ord('A')))}",end = '')
