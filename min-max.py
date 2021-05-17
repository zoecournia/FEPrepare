#!/usr/bin/python
import sys
import os
import difflib

fileA = sys.argv[1]
fileB = sys.argv[2]
with open('complex/min-max_center', 'w') as outfile:  
    with open(fileA) as infile:   
     lines = infile.read().splitlines()
     last_linea = lines[-4]
     last_lineb = lines[-3]
     outfile.write(last_linea)
     outfile.write("\n")
     outfile.write(last_lineb)
with open('solvent/min-max_center', 'w') as outfile2:  
    with open(fileB) as infile2:  
     lines2 = infile2.read().splitlines()
     last_line2a = lines2[-4]
     last_line2b = lines2[-3]
     outfile2.write(last_line2a)
     outfile2.write("\n")
     outfile2.write(last_line2b)
