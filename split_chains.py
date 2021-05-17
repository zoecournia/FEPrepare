#!/usr/bin/python
import sys
import os
import difflib

fileA = sys.argv[1]
fileB = sys.argv[2]

atom1=[];atom_lines1=0;four=[];five=[];
atom2=[];atom_lines2=0;
with open(fileA, 'r') as infile:
  with open(fileB,'r') as infile2:
    while True:

      line1 = infile.readline().strip()
      if line1.startswith('ATOM'): 
        atom_lines1=atom_lines1+1
        atom1.append(line1)

      line2 = infile2.readline().strip()
      if line2.startswith('ATOM'):
        atom_lines2=atom_lines2+1
        atom2.append(line2)

      if line1.startswith('END') and line2.startswith('TER'):
        break;
      if line1 == '' and line2 == '':
        break;

for i in range(atom_lines1):
    atomdata = atom1[i]
    atomdata = atomdata.split()
    
    five.append(atomdata[4])
    
for j in range(atom_lines2):
    atomdata2 = atom2[j]
    atomdata2 = atomdata2.split()
    
    four.append(atomdata[3])
   
fi=list(set(five))
fo=list(set(four))
for i in fi:
  if i.isdigit() : 
    fi.remove(i)
####printing files for VMD
with open('psfgen','w') as outfile:
  outfile.write("mol delete all\n")
  outfile.write("mol load pdb ../complex.pdb\n")
  outfile.write("set bad [atomselect top \"resname ACE\"]\n")
  outfile.write("if {[info exists bad]} {\n")
  for i in range(len(fi)):
    outfile.write("set chain%s " %fi[i])
    outfile.write("[atomselect top \"chain %s and not hydrogen and not resname ACE NME\"]\n" %fi[i])
  outfile.write("set chainX [atomselect top \"residuetype nothing and not resname ACE NME\"]\n")
  outfile.write("set flag 1\n")
  outfile.write("} else {\n")
  for i in range(len(fi)):
    outfile.write("set chain%s " %fi[i]) 
    outfile.write("[atomselect top \"chain %s and not hydrogen\"]\n" %fi[i])
  outfile.write("set chainX [atomselect top \"residuetype nothing\"]\n")  
  outfile.write("set flag 0}\n")
  for i in range(len(fi)):
    outfile.write("$chain%s writepdb "%fi[i])
    outfile.write("chain%s.pdb\n"%fi[i])
  outfile.write("$chainX writepdb chainX.pdb\n")
  outfile.write("package require psfgen\n")
  outfile.write("topology ../top_opls_aam.inp\n")
  outfile.write("topology ../ligand.rtf\n")
  outfile.write("pdbalias HIS HSD\n")
  outfile.write("pdbalias atom SER HG HG1\n")
  outfile.write("pdbalias residue HIS HSE\n")
  outfile.write("pdbalias atom ILE CD1 CD\n")
  outfile.write("if {$flag == 1} {\n")
  for i in range(len(fi)):
    outfile.write("segment %s {\n" %fi[i])
    outfile.write("  first ACE\n")
    outfile.write("  last CT3\n")
    outfile.write("  pdb chain%s.pdb\n" %fi[i])
    outfile.write("}\n")
  outfile.write("} else {\n")
  for i in range(len(fi)):
    outfile.write("segment %s {\n" %fi[i])
    outfile.write("  first NONE\n")
    outfile.write("  last NONE\n")
    outfile.write("  pdb chain%s.pdb\n" %fi[i])
    outfile.write("}\n")
  outfile.write("}\n")
  outfile.write("segment X {\n")
  outfile.write("  first NONE\n")
  outfile.write("  last NONE\n")
  outfile.write("  pdb chainX.pdb\n" )
  outfile.write("}\n")
  for i in range(len(fi)):
    outfile.write("coordpdb chain%s.pdb " %fi[i])
    outfile.write("%s\n" %fi[i])
  outfile.write("coordpdb chainX.pdb X\n")
  outfile.write("guesscoord\n")
  outfile.write("regenerate angles dihedrals\n")
  outfile.write("writepdb psf-complex.pdb\n")
  outfile.write("writepsf psf-complex.psf\n")
  outfile.write("exit")
   

#with open('chains','w') as outfile:
 # outfile.write("%s\n" %fi)
  #outfile.write("%s" %fo)
#print(fi)
#print (fo)
#print(y)
#chain=[];
#with open('chains','r') as infile3:
 #while True:

  #    line = infile3.readline().strip()
   #   l=l+1
    #  chain.append(line)
     # if line=='':
      #  break;    
#for i in range(l):
 # chaindata = chain[1]
  #chaindata = chaindata.split()
  #if chaindata[i]=='[' or chaindata[i]==',' or chaindata[i]=="'":
   #    continue;
  #else
   #    chaindata[i]
#print line
infile.close()
infile2.close()
outfile.close()
#infile3.close()
