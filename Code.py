#!/usr/bin/python

###
#
# Header
# Author Vincent Misson
# Un peu plus de code !
# Mais pas trop
#
###


import sys
import gzip
import time

print("\n")
print("Uggla special code !")
print("--------------------\n\n")

with gzip.open('ascii.txt.gz', 'rb') as f:
        file_content = f.read()

print(file_content)
time.sleep(3)

while (True):
    sys.stdout.write("'")
