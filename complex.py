#Complex file = hybrid.pdb + protein.pdb
#Stamatia Zavitsanou
#to execute type in command line python complex.py

#!/usr/bin/python
import sys
import os
import difflib

ena=[];second=[];one=[];first2=[];second2=[]
third2=[];fourth2=[];fifth2=[];sixth2=[];seventh2=[]
eightth2=[]

fileA = sys.argv[1]
with open('complex', 'w') as outfile:  ###auto tha pareis
    with open(fileA) as infile: 
        lines=infile.readlines()
        for i in range(0,len(lines)):
            line=lines[i]
            data = line.split()
            ena.append(data[0])
            if line.startswith('ATOM'):
                second.append(data[1])
                
            if ena[i]!='END':
                outfile.write(line)
            else:
                outfile.write("TER\n")
                print("LUL")
                with open('hybridpdb.txt') as infile2:  ####allazeis edw, to pairneis apo to dual2
                    lines2=infile2.readlines()

                    for i in range(0,len(lines2)):
                        line2=lines2[i]
                        data2 = line2.split()

                        if line2.startswith("REMARK"):
                            continue;
                        else:
                            first2.append(data2[0])
                            second2.append(len(second)+1+i)
                            third2.append(data2[2])
                            fourth2.append(data2[3])
                            fifth2.append(data2[4])
                            sixth2.append(data2[5])
                            seventh2.append(data2[6])
                            eightth2.append(data2[7])
                            #seventh2.append(data2[8])
                    for i in range(len(second2)):
                            outfile.write("%4s" %(first2[i]))
                            outfile.write("%7s" %(second2[i]))
                            outfile.write("%5s" %(third2[i]))
                            outfile.write("%4s" %(fourth2[i]))
                            outfile.write("%6s" %(fifth2[i]))
                            outfile.write("%12s" %(sixth2[i]))
                            outfile.write("%8s" %(seventh2[i]))
                            outfile.write("%8s\n" %(eightth2[i]))
                    outfile.write("TER\n")
                    outfile.write("END\n")
#sumatoms=len(second)
#print(second)
