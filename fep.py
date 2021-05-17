#update fep files.
#Stamatia Zavitsanou
#to execute type in command line python fep1.py

#!/usr/bin/python
import sys
import os
import difflib
import d
import string

com = sys.argv[1] 
sol = sys.argv[2]
pdbcom = sys.argv[3]
pdbsol = sys.argv[4]
############################################################
lines=0;lines2=0;lines3=0;lines4=0;data=[];data2=[]
linespdb=0;x1=[];y1=[];z1=[];x2=[];y2=[];z2=[];j=0;k=0
thirdcom=[];thirdsol=[];new=[];new2=[];upper2=[];upper3=[]
###########################################################
print(d.lateruse)
for i in range(len(d.lateruse)):
    if (d.lateruse[i]).startswith('A'):
      n = (d.lateruse[i]).strip()
      new.append(n[1]+n[2]+n[3])

    if (d.lateruse[i]).startswith('B'):
      n2 = (d.lateruse[i]).strip()     
      new2.append(n2[1]+n2[2]+n2[3])
print (new)
print (new2)
for i in range(len(new)):
   upper2.append(new[i].upper())
for i in range(len(new2)):
   upper3.append(new2[i].upper())
###########################################################
with open(com) as f1:
 with open('ionized_complex.fep', 'w') as outfile:
  for line1 in f1:
    line1 = line1.strip()
    flaga=0
    if line1.startswith('ATOM'):
        lines=lines+1
        dataatom = line1.split()
        f=dataatom[4]
        if f=='X':
         oh=dataatom[2]
         ohh=oh.strip()
##if there is a Cl or Br in the file probably the coordinates are wrong so we gotta write them correctly from ligand.pdb file
         if ohh[1].isalpha(): 
            flaga=1
            pdb=open('ligand.pdb', 'r')
            for linepdb in pdb:
                linepdb = linepdb.strip()
    
                if linepdb.startswith('ATOM'):
                 linespdb=linespdb+1
                 dataatompdb = linepdb.split()
                 ohpdb=dataatompdb[2]
                 if ohpdb[1].isalpha():
                  print ohpdb[1]
                  o=ohpdb[0]
                  t=ohpdb[1]
                  x1.append(dataatompdb[5])
                  y1.append(dataatompdb[6])
                  z1.append(dataatompdb[7])
         upper=dataatom[2].upper()
         
         if dataatom[2] in new or upper in upper2:  
            
            if flaga==1:
              if len(x1)<=1:
                  j=0
              for i in range(len(x1)):
                  outfile.write("%4s" %(dataatom[0]))
                  outfile.write("%7s" %(dataatom[1]))
                  outfile.write("%5s" %(dataatom[2]))
                  outfile.write("%4s" %(dataatom[3]))
                  outfile.write("%2s" %(dataatom[4]))
                  outfile.write("%4s" %(dataatom[5]))
                  outfile.write("%12s" %(x1[j]))
                  outfile.write("%8s" %(y1[j]))
                  outfile.write("%8s" %(z1[j]))
                  outfile.write("%6s" %("1.00"))
                  outfile.write("%6s" %("-1.00"))
                  outfile.write("%7s" %(dataatom[11]))
                  outfile.write("%5s\n" %(o+t))
                  j=j+1
                  break;
                  
            else:
              outfile.write("%4s" %(dataatom[0]))
              outfile.write("%7s" %(dataatom[1]))
              outfile.write("%5s" %(dataatom[2]))
              outfile.write("%4s" %(dataatom[3]))
              outfile.write("%2s" %(dataatom[4]))
              outfile.write("%4s" %(dataatom[5]))
              outfile.write("%12s" %(dataatom[6]))
              outfile.write("%8s" %(dataatom[7]))
              outfile.write("%8s" %(dataatom[8]))
              outfile.write("%6s" %(dataatom[9]))
              outfile.write("%6s" %("-1.00"))
              outfile.write("%7s" %(dataatom[11]))
              outfile.write("%5s\n" %(dataatom[12]))
            
         elif dataatom[2] in new2 or upper in upper3:
            
            if flaga==1:
              if len(x1)<=1:
                j=0
              for i in range(len(x1)):
                  outfile.write("%4s" %(dataatom[0]))
                  outfile.write("%7s" %(dataatom[1]))
                  outfile.write("%5s" %(dataatom[2]))
                  outfile.write("%4s" %(dataatom[3]))
                  outfile.write("%2s" %(dataatom[4]))
                  outfile.write("%4s" %(dataatom[5]))
                  outfile.write("%12s" %(x1[j]))
                  outfile.write("%8s" %(y1[j]))
                  outfile.write("%8s" %(z1[j]))
                  outfile.write("%6s" %("1.00"))
                  outfile.write("%6s" %("1.00"))
                  outfile.write("%7s" %(dataatom[11]))
                  outfile.write("%5s\n" %(o+t))
                  j=j+1
                  break;
                  
            else:
                  outfile.write("%4s" %(dataatom[0]))
                  outfile.write("%7s" %(dataatom[1]))
                  outfile.write("%5s" %(dataatom[2]))
                  outfile.write("%4s" %(dataatom[3]))
                  outfile.write("%2s" %(dataatom[4]))
                  outfile.write("%4s" %(dataatom[5]))
                  outfile.write("%12s" %(dataatom[6]))
                  outfile.write("%8s" %(dataatom[7]))
                  outfile.write("%8s" %(dataatom[8]))
                  outfile.write("%6s" %(dataatom[9]))
                  outfile.write("%6s" %("1.00"))
                  outfile.write("%7s" %(dataatom[11]))
                  outfile.write("%5s\n" %(dataatom[12]))
    
         else:
            outfile.write("%s\n" %(line1))
        else:
            outfile.write("%s\n" %(line1))  
    else:
        outfile.write("%s\n" %(line1))
        
    if line1 =='':
        break;
############################################################################
with open(sol) as f2:
 with open('ionized_solvent.fep', 'w') as outfile2:
  for line2 in f2:
    line2 = line2.strip() 
    flagb=0
    if line2.startswith('ATOM'):
        lines2=lines2+1
        dataatom2= line2.split() 
        f=dataatom2[4]
        if f=='X':
         oh2=dataatom2[2]
         ohh2=oh2.strip()
##if there is a Cl or Br in the file probably the coordinates are wrong so we gotta write them correctly from ligand.pdb file
         if ohh2[1].isalpha(): 
            flagb=1
            pdb=open('ligand.pdb', 'r')
            for linepdb in pdb:
                linepdb = linepdb.strip()
    
                if linepdb.startswith('ATOM'):
                 linespdb=linespdb+1
                 dataatompdb = linepdb.split()
                 ohpdb=dataatompdb[2]
                 if ohpdb[1].isalpha():
                  o=ohpdb[0]
                  t=ohpdb[1]
                  x1.append(dataatompdb[5])
                  y1.append(dataatompdb[6])
                  z1.append(dataatompdb[7])
         upper=dataatom2[2].upper()
         if dataatom2[2] in new or upper in upper2:  
            if flagb==1:
              if len(x1)<=1:
                  j=0
              for i in range(len(x1)):
                  outfile2.write("%4s" %(dataatom2[0]))
                  outfile2.write("%7s" %(dataatom2[1]))
                  outfile2.write("%5s" %(dataatom2[2]))
                  outfile2.write("%4s" %(dataatom2[3]))
                  outfile2.write("%2s" %(dataatom2[4]))
                  outfile2.write("%4s" %(dataatom2[5]))
                  outfile2.write("%12s" %(x1[j]))
                  outfile2.write("%8s" %(y1[j]))
                  outfile2.write("%8s" %(z1[j]))
                  outfile2.write("%6s" %("1.00"))
                  outfile2.write("%6s" %("-1.00"))
                  outfile2.write("%7s" %(dataatom2[11]))
                  outfile2.write("%5s\n" %(o+t))
                  j=j+1
                  break;
                  
            else:
              outfile2.write("%4s" %(dataatom2[0]))
              outfile2.write("%7s" %(dataatom2[1]))
              outfile2.write("%5s" %(dataatom2[2]))
              outfile2.write("%4s" %(dataatom2[3]))
              outfile2.write("%2s" %(dataatom2[4]))
              outfile2.write("%4s" %(dataatom2[5]))
              outfile2.write("%12s" %(dataatom2[6]))
              outfile2.write("%8s" %(dataatom2[7]))
              outfile2.write("%8s" %(dataatom2[8]))
              outfile2.write("%6s" %(dataatom2[9]))
              outfile2.write("%6s" %("-1.00"))
              outfile2.write("%7s" %(dataatom2[11]))
              outfile2.write("%5s\n" %(dataatom2[12]))
            
         elif dataatom2[2] in new2 or upper in upper3:
            if flagb==1:
             if len(x1)<=1:
              j=0
             for i in range(len(x1)):
              outfile2.write("%4s" %(dataatom2[0]))
              outfile2.write("%7s" %(dataatom2[1]))
              outfile2.write("%5s" %(dataatom2[2]))
              outfile2.write("%4s" %(dataatom2[3]))
              outfile2.write("%2s" %(dataatom2[4]))
              outfile2.write("%4s" %(dataatom2[5]))
              outfile2.write("%12s" %(x1[j]))
              outfile2.write("%8s" %(y1[j]))
              outfile2.write("%8s" %(z1[j]))
              outfile2.write("%6s" %("1.00"))
              outfile2.write("%6s" %("1.00"))
              outfile2.write("%7s" %(dataatom2[11]))
              outfile2.write("%5s\n" %(o+t))
              j=j+1
              break;
            else:
             outfile2.write("%4s" %(dataatom2[0]))
             outfile2.write("%7s" %(dataatom2[1]))
             outfile2.write("%5s" %(dataatom2[2]))
             outfile2.write("%4s" %(dataatom2[3]))
             outfile2.write("%2s" %(dataatom2[4]))
             outfile2.write("%4s" %(dataatom2[5]))
             outfile2.write("%12s" %(dataatom2[6]))
             outfile2.write("%8s" %(dataatom2[7]))
             outfile2.write("%8s" %(dataatom2[8]))
             outfile2.write("%6s" %(dataatom2[9]))
             outfile2.write("%6s" %("1.00"))
             outfile2.write("%7s" %(dataatom2[11]))
             outfile2.write("%5s\n" %(dataatom2[12]))
     
            
         else:
            outfile2.write("%s\n" %(line2))
        else:
            outfile2.write("%s\n" %(line2))
    else:
        outfile2.write("%s\n" %(line2))
        
    if line2 =='':
        break;
#########################################################################
with open(pdbcom) as f3:
 with open('ionized_complex.pdb', 'w') as outfile3:
  for line3 in f3:
    line3 = line3.strip()
    flagc=0
    if line3.startswith('ATOM'):
        lines3=lines3+1
        dataatom3= line3.split() 
        f=dataatom3[4]
        if f=='X':
         oh3=dataatom3[2]
         ohh3=oh3.strip()
##if there is a Cl or Br in the file probably the coordinates are wrong so we gotta write them correctly from ligand.pdb file
         if ohh3[1].isalpha(): 
            flagc=1
            pdb=open('ligand.pdb', 'r')
            for linepdb in pdb:
                linepdb = linepdb.strip()
    
                if linepdb.startswith('ATOM'):
                 linespdb=linespdb+1
                 dataatompdb = linepdb.split()
                 ohpdb=dataatompdb[2]
                 if ohpdb[1].isalpha():
                  o=ohpdb[0]
                  t=ohpdb[1]
                  x1.append(dataatompdb[5])
                  y1.append(dataatompdb[6])
                  z1.append(dataatompdb[7])
         upper=dataatom3[2].upper()
         if dataatom3[2] in new or upper in upper2:  
            if flagc==1:
              if len(x1)<=1:
                  k=0
              for i in range(len(x1)):
                  outfile3.write("%4s" %(dataatom3[0]))
                  outfile3.write("%7s" %(dataatom3[1]))
                  outfile3.write("%5s" %(dataatom3[2]))
                  outfile3.write("%4s" %(dataatom3[3]))
                  outfile3.write("%2s" %(dataatom3[4]))
                  outfile3.write("%4s" %(dataatom3[5]))
                  outfile3.write("%12s" %(x1[k]))
                  outfile3.write("%8s" %(y1[k]))
                  outfile3.write("%8s" %(z1[k]))
                  outfile3.write("%6s" %("1.00"))
                  outfile3.write("%6s" %(dataatom3[10]))
                  outfile3.write("%7s" %(dataatom3[11]))
                  outfile3.write("%5s\n" %(o+t))
                  k=k+1
                  break;
                  
            else:
              outfile3.write("%s\n" %(line3))
            
         elif dataatom3[2] in new2 or upper in upper3:
            if flagc==1:
             if len(x1)<=1:
                  k=0
             for i in range(len(x1)):
              outfile3.write("%4s" %(dataatom3[0]))
              outfile3.write("%7s" %(dataatom3[1]))
              outfile3.write("%5s" %(dataatom3[2]))
              outfile3.write("%4s" %(dataatom3[3]))
              outfile3.write("%2s" %(dataatom3[4]))
              outfile3.write("%4s" %(dataatom3[5]))
              outfile3.write("%12s" %(x1[k]))
              outfile3.write("%8s" %(y1[k]))
              outfile3.write("%8s" %(z1[k]))
              outfile3.write("%6s" %("1.00"))
              outfile3.write("%6s" %(dataatom3[10]))
              outfile3.write("%7s" %(dataatom3[11]))
              outfile3.write("%5s\n" %(o+t))
              k=k+1
              break;
            else:
             outfile3.write("%s\n" %(line3))
         else:
              outfile3.write("%s\n" %(line3))
        else:
            outfile3.write("%s\n" %(line3)) 
    else:
        outfile3.write("%s\n" %(line3))
        
    if line3 =='':
        break;
##########################################################################
with open(pdbsol) as f4:
 with open('ionized_solvent.pdb', 'w') as outfile4:
  for line4 in f4:
    line4 = line4.strip()
    flagd=0
    if line4.startswith('ATOM'):
        lines4=lines4+1
        dataatom4= line4.split() 
        f=dataatom4[4]
        if f=='X':
         oh4=dataatom4[2]
         ohh4=oh4.strip()
##if there is a Cl or Br in the file probably the coordinates are wrong so we gotta write them correctly from ligand.pdb file
         if ohh4[1].isalpha(): 
            flagd=1
            pdb=open('ligand.pdb', 'r')
            for linepdb in pdb:
                linepdb = linepdb.strip()
    
                if linepdb.startswith('ATOM'):
                 linespdb=linespdb+1
                 dataatompdb = linepdb.split()
                 ohpdb=dataatompdb[2]
                 if ohpdb[1].isalpha:
                  o=ohpdb[0]
                  t=ohpdb[1]
                  x1.append(dataatompdb[5])
                  y1.append(dataatompdb[6])
                  z1.append(dataatompdb[7])
         upper=dataatom4[2]
         if dataatom4[2] in new or upper in upper2:  
            if flagd==1:
              if len(x1)<=1:
                  k=0
              for i in range(len(x1)):
                  outfile4.write("%4s" %(dataatom4[0]))
                  outfile4.write("%7s" %(dataatom4[1]))
                  outfile4.write("%5s" %(dataatom4[2]))
                  outfile4.write("%4s" %(dataatom4[3]))
                  outfile4.write("%2s" %(dataatom4[4]))
                  outfile4.write("%4s" %(dataatom4[5]))
                  outfile4.write("%12s" %(x1[k]))
                  outfile4.write("%8s" %(y1[k]))
                  outfile4.write("%8s" %(z1[k]))
                  outfile4.write("%6s" %("1.00"))
                  outfile4.write("%6s" %(dataatom3[10]))
                  outfile4.write("%7s" %(dataatom3[11]))
                  outfile4.write("%5s\n" %(o+t))
                  k=k+1
                  break;
                  
            else:
              outfile4.write("%s\n" %(line4))
            
         elif dataatom4[2] in new2 or upper in upper3:
            if flagd==1:
             if len(x1)<=1:
                  k=0
             for i in range(len(x1)):
              outfile4.write("%4s" %(dataatom4[0]))
              outfile4.write("%7s" %(dataatom4[1]))
              outfile4.write("%5s" %(dataatom4[2]))
              outfile4.write("%4s" %(dataatom4[3]))
              outfile4.write("%2s" %(dataatom4[4]))
              outfile4.write("%4s" %(dataatom4[5]))
              outfile4.write("%12s" %(x1[k]))
              outfile4.write("%8s" %(y1[k]))
              outfile4.write("%8s" %(z1[k]))
              outfile4.write("%6s" %("1.00"))
              outfile4.write("%6s" %(dataatom4[10]))
              outfile4.write("%7s" %(dataatom4[11]))
              outfile4.write("%5s\n" %(o+t))
              k=k+1
              break;
            else:
             outfile4.write("%s\n" %(line4))
         else:
              outfile4.write("%s\n" %(line4))
        else:
            outfile4.write("%s\n" %(line4)) 
    else:
        outfile4.write("%s\n" %(line4))
        
    if line4 =='':
        break;

f1.close()
f2.close()
f3.close()
f4.close()
