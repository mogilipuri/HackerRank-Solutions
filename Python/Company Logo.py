#!/bin/python3

import math
import os
import random
import re
import sys
str1=input("")
d= dict()
for letter in str1:
    d[letter]=d.get(letter,0)+1
l=list(d.values())
keys=list(d.keys())
keys.sort()
count=0
while count<3:
    b=max(l)
    for i in keys:
        if d[i]==b:
            print(i,d[i])
            count=count+1
            if count==3:
                break
            l.pop(l.index(max(l)))
