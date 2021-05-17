#Dual Topology Builder , hybrid files , updated prm
#Stamatia Zavitsanou
#to execute type in command line python topology.py

#!/usr/bin/python
import sys
import os
import difflib

############################################  ALL THE DUAL ################################################
def percentage(fo1,fo2,diff):
   #calculating the difference between the two values
   if abs(fo2-fo1)>= diff:
       return 0
   else:
       return 1

#########

def ola(atom_lines1,atom_lines2,firstatom2,secondatom2,thirdatom2,fourthatom2,firstatom,secondatom,thirdatom,fourthatom,diff):
 p=0;l=0;sumA=0;sumB=0;n_linesA=0;n_linesB=0;n_lines=0
 m2=0;m=0;m3=0;sumA=0;sumB=0;divround=0;divabs=0
 name=[];name2=[]

 for a2 in range(atom_lines2):
    if secondatom2[a2] in secondatom :  #the two second words are the same so we have to check their values
      print("we are the same")
      m=fourthatom[a2]
      m=float(m)
      m2=fourthatom2[a2]
      m2=float(m2)
      
      x = percentage(m,m2,diff)
      if x == 1:  #they differ less than 10% so no need to do anything
            print("ouf")
            #stay as they are
      else:
            print("ta m einai")
            print (m,m2)
            print("oups") # the differ more than 0.1
            new.write("A %s " %(firstatom[a2]))
            new.write("%s " %(secondatom[a2]))
            name.append(secondatom[a2])
            new.write("%s " %(thirdatom[a2]))
            new.write("%s\n" %(fourthatom[a2]))
            sumA=sumA+m
            print("sumA",sumA)
            n_linesA=n_linesA+1 

            new.write("B %s " %(firstatom2[a2]))
            new.write("%s " %(secondatom2[a2]))
            name2.append(secondatom2[a2])
            new.write("%s " %(thirdatom2[a2]))
            new.write("%s\n" %(fourthatom2[a2]))
            sumB=sumB+m2
            print("sumB",sumB)
            n_linesB=n_linesB+1
      print(secondatom[a2])
    if secondatom2[a2] not in secondatom:

           print("ta m einai")
           print (m,m2)
           new.write("B %s " %(firstatom2[a2]))
           new.write("%s " %(secondatom2[a2]))
           name2.append(secondatom2[a2])
           new.write("%s " %(thirdatom2[a2]))
           new.write("%s\n" %(fourthatom2[a2]))
           fatom2=float(fourthatom2[a2])
           sumB=sumB+fatom2
           print("sumB",sumB)
           n_linesB=n_linesB+1

 for a in range(atom_lines1):
    if secondatom[a] not in secondatom2:

       new.write("A %s " %(firstatom[a]))
       new.write("%s " %(secondatom[a]))
       name.append(secondatom[a])
       new.write("%s " %(thirdatom[a]))
       new.write("%s\n" %(fourthatom[a]))
       fatom1=float(fourthatom[a])
       sumA=sumA+fatom1
       print("sumA",sumA)
       n_linesA=n_linesA+1
 n_lines=n_linesA+n_linesB
 print(n_lines)

 extra=[];extra2=[]
 for b in range (bondsum2):
    databond2 = bond2[b]
    databond2 = databond2.split()

    firstbond2.append(databond2[0])
    secondbond2.append(databond2[1])
    thirdbond2.append(databond2[2])

    sec2=secondbond2[b].strip()
    asec2=sec2[0]
    
    thir2=thirdbond2[b].strip()
    athir2=thir2[0]

    for i in range(len(name2)):
        if secondbond2[b]==name2[i]:
            if athir2 == 'H' and thirdbond2[b] not in name2:
              extra2.append(thirdbond2[b])
        if thirdbond2[b]==name2[i] and secondbond2[b] not in name2:
            if asec2=='H':
              extra2.append(secondbond2[b])
 for b in range (bondsum):
    databond = bond[b]
    databond = databond.split()

    firstbond.append(databond[0])
    secondbond.append(databond[1])
    thirdbond.append(databond[2])

    sec=secondbond[b].strip()
    asec=sec[0]
    
    thir=thirdbond[b].strip()
    athir=thir[0]

    for i in range(len(name)):               
        if secondbond[b]==name[i] and thirdbond[b] not in name:
            if athir == 'H':
              extra.append(thirdbond[b])
        if thirdbond[b]==name[i] and secondbond[b] not in name:
            if asec=='H':
              extra.append(secondbond[b])
 print(extra,extra2)
 extracharge=[];extracharge2=[]
 for i in range(len(extra)):
    for j in range(atom_lines1):
     if extra[i]==secondatom[j]:
      extracharge.append(fourthatom[j])
      fatom1=float(fourthatom[j])
      new.write("A %s " %(firstatom[j]))
      new.write("%s " %(secondatom[j]))
      new.write("%s " %(thirdatom[j]))
      new.write("%s\n" %(fourthatom[j]))
      print(fatom1)
      sumA=fatom1+sumA
 n_linesA=n_linesA+len(extra)

 for i in range(len(extra2)):
    for j in range(atom_lines2):
     if extra2[i]==secondatom2[j]:
      extracharge2.append(fourthatom2[j])
      fatom2=float(fourthatom2[j])
      new.write("B %s " %(firstatom2[j]))
      new.write("%s " %(secondatom2[j]))
      new.write("%s " %(thirdatom2[j]))
      new.write("%s\n" %(fourthatom2[j]))
      print(fatom2)
      sumB=fatom2+sumB
 n_linesB=n_linesB+len(extra2)
 n_lines=n_linesA+n_linesB
 print("edw eimai",n_lines)
 
 print(sumA)
 print(sumB)
 print(n_linesB)
 print(extracharge,extracharge2)
 value=sumB-sumA
 div=value/n_linesB
 print (div)
 divabs=abs(div)
 divround=round(divabs,2)
 print (divround)

 if(divround>0.02):
   print ("div is too big")
   diff=diff-0.01
   print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",diff)
   new.write("\n")
   n_lines,div=ola(atom_lines1,atom_lines2,firstatom2,secondatom2,thirdatom2,fourthatom2,firstatom,secondatom,thirdatom,fourthatom,diff)
   
 else:
   print(n_lines,div)
   return(n_lines,div)
 print(n_lines,div)
 return(n_lines,div)

##########

def update_charges(n,chargaki):
  firstb=[];secondb=[];thirdb=[];fourthb=[];fifthb=[];B=[];batom=[];A=[];thirda=[]
  newfifthb=[]
  Bsum=0;Asum=0
  new = open('dothemath.txt','r')
  for line in (new.readlines() [-n:]):
     print(line)
     if line.startswith ('B'):
       Bsum=Bsum+1
       B.append(line)
       #print(line)
     if line.startswith ('A'):
       Asum=Asum+1
       A.append(line)
  for b in range(Bsum):
    datab= B[b]
    datab = datab.split()

    firstb.append(datab[0])
    secondb.append(datab[1])
    thirdb.append(datab[2])
    fourthb.append(datab[3])
    fifthb.append(datab[4])
    newfifthb.append(float(datab[4])+chargaki)
  print(newfifthb)
  for a in range(Asum):
    dataa= A[a]
    dataa = dataa.split()
    thirda.append(dataa[2])
  return(thirdb,fourthb,newfifthb,thirda)

#####################################NEW NAMES MUTATIONS ONLY################################################

def change_names(thirdb,fourthb,secondatom,thirdatom):
    
    print(secondatom)
    three2=[];four2=[];a=[];b=[];c=[];asecond=[];bsecond=[];csecond=[];cc=0;ccc=0;oo=[];po=0;flag=0;flag2=0
    athird=[];bthird=[];cthird=[];dthird=[];fa=[];fb=[];fc=[];fd=[];l2=[];l3=[];l4=[];l5=[];l6=[]
    a2=[];b2=[];c2=[]
    for i in range(len(secondatom)):
        s=secondatom[i].strip()
        asecond.append(s[0])
        bsecond.append(s[1])
        csecond.append(s[2])
    print thirdb
    for j in range(len(thirdb)):
        t=thirdb[j].strip()
        a.append(t[0])
        b.append(t[1])
        c.append(t[2])
    with open ("how_many") as infile:
         for l in infile:
             print l
             l1=l.split("]")
         for i in range(len(l1)):
             l2.append(l1[i].replace("[",""))
         for i in range(len(l2)):
	     l3.append(l2[i].replace(",",""))
	 for i in range(len(l3)):
	     l4.append(l3[i].replace(" ",""))
         for i in range(len(l4)):
	     l6.append(l4[i].replace("'",""))
         print ("l6",l6)
         for i in range(len(l6)):
             if l6[i]=='':
               continue
             else:
               l5.append(l6[i])
               oo.append(len(l6[i]))
	 print oo,l5

    for j in range(len(thirdb)):
         if thirdb[j] not in secondatom:
            ola=[a[j],b[j],c[j]]
            newt=''.join(ola)
            three2.append(newt)
      
         else:
          for i in range(len(secondatom)):
           if secondatom[i]==thirdb[j]:
           
             if bsecond[i].isalpha() :
                print ("lolololol",bsecond[i])
                cc=csecond[i]
                cc=int(cc)+1
                cc=str(cc)
                ola=[a[j],b[j],cc]
                newt=''.join(ola)
                three2.append(newt)
             else:
	        
	        for f in range(len(l5)):
                  print ("j",j)
		  print ("lllllllllllllll",b[j])
		  if b[j].isalpha():
                    continue;
                  else:
                   
                   print ("kkkkk",l5[f][0])
                   if l5[f][0]==a[j]:
		      print a[j]
		      print b[j]
		      print("ti leei?")
		      if oo[f]==2:
                        w1=l5[f][1]
                        flag=flag+1
                        print w1,flag
                        if flag>1:
                         w1=w1a
                        print "einai"
                        print("mpika?")
                        print l5[f][0]
		       #w1=l5[f][1]
		        w1a=int(w1)+flag
		        w1a=str(w1)
		        ola=[a[j],'0',w1a]
		        newt=''.join(ola)
                        print newt
		        three2.append(newt)
                      else:
                       w1=l5[f][1]
                       w11=l5[f][2]
                       flag2=flag2+1
                       print w1,w11,flag2
                       if flag2 >1:
                        w1=w1b
                        w11=w11b
		        print (l5[f][2])
		        print("edw?")
		       #w11=l5[f][2]
		        print ("w11",w11)
		       #w1=l5[f][1]
                       print("dddddd",int(w11)+flag2)
		       if (int(w11)+flag2)>9:
		        w1b=int(w1)+1
		        w11b=0
                        print "twra"
		       else:
		        w11b=int(w11)+flag2
                        w1b=w1
		        print ("poso",w11)
		       w1b=str(w1b)
		       w11b=str(w11b)
		       ola=[a[j],w1b,w11b]
		       newt=''.join(ola)
                       print newt
		       three2.append(newt)
		      
    print ("three2",three2)
    print fourthb
    for u in range(len(three2)):
       t2=three2[u].strip()
       a2.append(t2[0])
       b2.append(t2[1])
       c2.append(t2[2])
    print a2,b2,c2
    for l in range(len(a2)):
       if b2[l].isalpha():
          ola=[a2[l],b2[l],'5',c2[l]]
	  newt=''.join(ola)
          four2.append(newt)
       else:
          ola=[a2[l],'5',b2[l],c2[l]]
	  newt=''.join(ola)
          four2.append(newt)
    #for u in range(len(thirdatom)):
     #   th=thirdatom[u].strip()
      #  athird.append(th[0])
       # bthird.append(th[1])
        #cthird.append(th[2])
        #dthird.append(th[3])
        #if bthird[u].isalpha():
         #  ccc=cthird[i]
    #print cthird
    #print dthird
    #ww=int(cthird[-1])
    #ww1=int(dthird[-1])
    #print ww,ww1
    #for j in range(len(fourthb)):
     #   f=fourthb[j].strip()
      #  fa.append(f[0])
       # fb.append(f[1])
        #fc.append(f[2])
        #fd.append(f[3])
        #if fb[j].isalpha():
         #   ccc=int(ccc)+1
          #  ccc=str(ccc)
           # ola=[a[j],b[j],'5',ccc]
            #newt=''.join(ola)
            #four2.append(newt)
        #else:
         #   ww1=int(ww1)+1  
          #  if ww1>9:
           #   ww=int(ww)+1
            #  ww1=0
            #ww=str(ww)
            #ww1=str(ww1)
            #ola=[a[j],'5',ww,ww1]
            #newt=''.join(ola)
            #four2.append(newt)
    print(three2,four2)
    return(three2,four2)

##############################################  HYBRID RTF  ###################################################

def new_atoms(firstatom2,three2,four2,five,firstmass2,secondmass2,thirdmass2,fourthmass2,fifthmass2,firstbond2,secondbond2,thirdbond2,
firstimpr2,secondimpr2,thirdimpr2,fourthimpr2,fifthimpr2):
  with open("newligandArtf.txt") as f:
    with open("final.txt", "w") as f1:
        lines=f.readlines()
        for i in range(0,len(lines)):
           line=lines[i]
           if line.startswith('MASS'):
                next=lines[i+1]
                if next.startswith('AUTO'):
                 f1.write(lines[i])
                 for i in range(len(secondmass2)):
                   f1.write("%s " %(firstmass2[i]))
                   f1.write("%s " %(secondmass2[i]))
                   f1.write("%s " %(thirdmass2[i]))
                   f1.write("%s " %(fourthmass2[i]))
                   f1.write("%s\n" %(fifthmass2[i]))
                else:
                   f1.write(line)
           elif line.startswith('ATOM'):
                next=lines[i+1]
                if next.startswith('BOND'):
                 f1.write(lines[i])
                 for i in range(len(three)):
                   f1.write("%s " %(firstatom2[i]))
                   f1.write("%s " %(three2[i]))
                   f1.write("%s " %(four2[i]))
                   f1.write("%s\n" %(five[i]))
                else:
                   f1.write(line)
           elif line.startswith('BOND'):
                next=lines[i+1]
                if next.startswith('IMPR'):
                 f1.write(lines[i])
                 for i in range(len(secondbond2)):
                   f1.write("%s " %(firstbond2[i]))
                   f1.write("%s " %(secondbond2[i]))
                   f1.write("%s\n" %(thirdbond2[i]))
                else:
                   f1.write(line)
           elif line.startswith('IMPR'):
                next=lines[i+1]
                if next.startswith('PATCH'):
                 f1.write(lines[i])
                 for i in range(len(secondimpr2)):
                   f1.write("%s " %(firstimpr2[i]))
                   f1.write("%s " %(secondimpr2[i]))
                   f1.write("%s " %(thirdimpr2[i]))
                   f1.write("%s " %(fourthimpr2[i]))
                   f1.write("%s\n" %(fifthimpr2[i]))
                else:
                   f1.write(line)
           else:
               f1.write(line)

#global later
def later(ta,tb):
   #lateruse=[]
   global lateruse
   lateruse=[]
   for i in range(len(ta)):
    lateruse.append("A"+ta[i])
    #lateruse.append(ta[i])
   for i in range(len(tb)):
    lateruse.append("B"+tb[i])
    #lateruse.append(tb[i])
##################################################################################################

#################################################################################################
################################## main #########################################################

#ligandA = sys.argv[1] 
ligandA = open('newligandArtf.txt','r')   ######ALLAZEIS EDWWW
#ligandB = sys.argv[2] 
ligandB = open('sortedB','r')             ######ALLAZEIS EDWWW auto pou exeis parei apo to merge2.py

new = open('dothemath.txt','w')    ###edw mporeis na elegxeis poia atoma tha paroun meros
 

atom_lines1=0;atom_lines2=0;atom_lines=0

mass=[];bond=[];impr=[];end=[];atom=[]
masssum=0;bondsum=0;imprsum=0;endsum=0

mass2=[];bond2=[];impr2=[];atom2=[]
masssum2=0;bondsum2=0;imprsum2=0;

#read the two rtf files 
while True:
    line1 = ligandA.readline().strip()   #this ligand we keep as it is. we change ligandB
    if line1.startswith('MASS'):
        masssum=masssum+1
        mass.append(line1)
    if line1.startswith('ATOM'):
        atom.append(line1)
        atom_lines1=atom_lines1+1
    if line1.startswith('BOND'):
        bondsum=bondsum+1
        bond.append(line1)
    if line1.startswith('IMPR'):
        imprsum=imprsum+1
        impr.append(line1)
    if line1 =='':
        break;

while True:
    line2 = ligandB.readline().strip()   
    if line2.startswith('MASS'):
        masssum2=masssum2+1
        mass2.append(line2)
    if line2.startswith('ATOM'):
        atom2.append(line2)
        atom_lines2=atom_lines2+1
    if line2.startswith('BOND'):
        bondsum2=bondsum2+1
        bond2.append(line2)
    if line2.startswith('IMPR'):
        imprsum2=imprsum2+1
        impr2.append(line2)
    if line2 == '':
        break;

#how many lines begin with the word ATOM
atom_lines=atom_lines1 + atom_lines2 
print (atom_lines)
print (masssum)
print (bondsum)
print (imprsum)

firstatom=[];secondatom=[];thirdatom=[];fourthatom=[]
firstatom2=[];secondatom2=[];thirdatom2=[];fourthatom2=[]
firstmass=[];secondmass=[];thirdmass=[];fourthmass=[];fifthmass=[]
firstmass2=[];secondmass2=[];thirdmass2=[];fourthmass2=[];fifthmass2=[]
firstbond2=[];secondbond2=[];thirdbond2=[]
firstbond=[];secondbond=[];thirdbond=[]
firstimpr=[];secondimpr=[];thirdimpr=[];fourthimpr=[];fifthimpr=[]
firstimpr2=[];secondimpr2=[];thirdimpr2=[];fourthimpr2=[];fifthimpr2=[]
for a in range(atom_lines1):
    dataatom = atom[a]
    dataatom = dataatom.split()

    firstatom.append(dataatom[0])
    secondatom.append(dataatom[1])
    thirdatom.append(dataatom[2])
    fourthatom.append(dataatom[3])

for a2 in range(atom_lines2):
    dataatom2 = atom2[a2]
    dataatom2 = dataatom2.split()

    firstatom2.append(dataatom2[0])
    secondatom2.append(dataatom2[1])
    thirdatom2.append(dataatom2[2])
    fourthatom2.append(dataatom2[3])

print(secondatom)
print(secondatom2)
oldthirdb=[];oldfourthb=[];threea=[];#lateruse=[]
#global lateruse
diff=0.1
lines,chargaki=ola(atom_lines1,atom_lines2,firstatom2,secondatom2,thirdatom2,fourthatom2,firstatom,secondatom,thirdatom,fourthatom,diff)
new.close()
chargaki=round(chargaki,2)
three,four,five,threea=update_charges(lines,chargaki)  ##adding the div to each charge

#lateruse.append("A")
#lateruse.append(threea)
three2,four2=change_names(three,four,secondatom,thirdatom)  ##giving new names to atoms
#lateruse.append("B")
#lateruse.append(three2)

later(threea,three2)
#print("llllllllllllllllllllllllll",lateruse)

##add the new atoms to ligandArtf in order to create the hybrid.
#print("llllllllllllllllllllllllll",three)

####################################### mass #################################################
i=0
firstmass22=[];secondmass22=[];thirdmass22=[];fourthmass22=[];fifthmass22=[];
for m in range(masssum2):
    datamass2 = mass2[m]
    datamass2 = datamass2.split()
    firstmass2.append(datamass2[0])
    secondmass2.append(datamass2[1])
    fourthmass2.append(datamass2[3])
    fifthmass2.append(datamass2[4])
    thirdmass2.append(datamass2[2])
    if thirdmass2[m]in four:
     for i in range(len(four)):
      if thirdmass2[m]== four[i]:
       thirdmass22.append(four2[i])
       i=i+1
       secondmass22.append(masssum+i)
       firstmass22.append(datamass2[0])
       fourthmass22.append(datamass2[3])###peirazei i seiroula?
       fifthmass22.append(datamass2[4])###
       
       #print(firstmass22,secondmass22,thirdmass22,fourthmass22,fifthmass22)
####################################### bond #################################################
firstbond22=[];secondbond22=[];thirdbond22=[]
for b in range (bondsum2):
    databond2 = bond2[b]
    databond2 = databond2.split()

    firstbond2.append(databond2[0])
    secondbond2.append(databond2[1])
    thirdbond2.append(databond2[2]) 


    if secondbond2[b] in three and thirdbond2[b] in three : 
        for i in range(len(three)):
         if thirdbond2[b]==three[i]:
           thirdbond22.append(three2[i]) 
     
         if secondbond2[b]==three[i]:
           firstbond22.append(databond2[0])
           secondbond22.append(three2[i]) 

    else: 
        for i in range(len(three)):
         if thirdbond2[b]==three[i]:
           firstbond22.append(databond2[0])
           secondbond22.append(databond2[1])
           thirdbond22.append(three2[i]) 
     
         if secondbond2[b]==three[i]:
           firstbond22.append(databond2[0])
           secondbond22.append(three2[i])
           thirdbond22.append(databond2[2]) 
#print(firstbond22,secondbond22,thirdbond22)

####################################### impr #################################################
firstimpr22=[];secondimpr22=[];thirdimpr22=[];fourthimpr22=[];fifthimpr22=[]

for im in range (imprsum2):
    
    dataimpr2 = impr2[im]
    dataimpr2 = dataimpr2.split()

    firstimpr2.append(dataimpr2[0])
    secondimpr2.append(dataimpr2[1])
    thirdimpr2.append(dataimpr2[2])
    fourthimpr2.append(dataimpr2[3])
    fifthimpr2.append(dataimpr2[4])

    if secondimpr2[im] in three and thirdimpr2[im] in three and fourthimpr2[im] in three and fifthimpr2[im] in three: 
        print("mpainei edw kale? mpaaaa")
        for i in range(len(three)):
         if thirdimpr2[im]==three[i]:
           thirdimpr22.append(three2[i]) 
     
         if secondimpr2[im]==three[i]:
           firstimpr22.append(dataimpr2[0])
           secondimpr22.append(three2[i]) 
         
         if fourthimpr2[im]==three[i]:
            fourthimpr22.append(three2[i])

         if fifthimpr2[im]==three[i]:
            fifthimpr22.append(three2[i])
    
    if secondimpr2[im] in three or thirdimpr2[im] in three or fourthimpr2[im] in three or fifthimpr2[im] in three: 
        
      print("mpainei edw kale? naiiii")
      firstimpr22.append(dataimpr2[0])

      if secondimpr2[im] in three:
        for i in range(len(three)):
          if secondimpr2[im] == three[i]:
           secondimpr22.append(three2[i])    
      else:
            secondimpr22.append(dataimpr2[1])
      
      if thirdimpr2[im] in three:
        for i in range(len(three)):
         if thirdimpr2[im] == three[i]:
           thirdimpr22.append(three2[i])    
      else:
            thirdimpr22.append(dataimpr2[2])
           
      if fourthimpr2[im] in three:
        for i in range(len(three)):
          if fourthimpr2[im] == three[i]:
           fourthimpr22.append(three2[i])           
      else:
            fourthimpr22.append(dataimpr2[3])

      if fifthimpr2[im] in three:
        for i in range(len(three)):
         if fifthimpr2[im] == three[i]:
           fifthimpr22.append(three2[i])
      else:       
             fifthimpr22.append(dataimpr2[4])

        
print(firstimpr22,secondimpr22,thirdimpr22,fourthimpr22,fifthimpr22)
new_atoms(firstatom2,three2,four2,five,firstmass22,secondmass22,thirdmass22,fourthmass22,fifthmass22,firstbond22,secondbond22,
thirdbond22,firstimpr22,secondimpr22,thirdimpr22,fourthimpr22,fifthimpr22)



###############################################################################################################################
######################################################## HYBRID PDB  ##########################################################
###############################################################################################################################

pdbA = open('newligandA.txt','r')   ###### ALLAZEIS EDWWW
pdbB = open('newligandB.txt','r')   ###### ALLAZEIS EDWWW

linesA=0;linesB=0;
atomA=[];atomB=[]
thirdatomB=[];firstatomB2=[];secondatomB2=[];fourthatomB2=[];fifthdatomB2=[];sixthatomB2=[];seventhhatomB2=[];eightthatomB2=[]
thirdatomB2=[];

while True:
    lineB = pdbB.readline().strip() 
    if lineB.startswith('ATOM'):
        linesB=linesB+1
        atomB.append(lineB)
    if lineB == '':
        break;

for a in range(linesB):
    dataatomB = atomB[a]
    dataatomB = dataatomB.split()

    thirdatomB.append(dataatomB[2])

    if thirdatomB[a]in three:
     for i in range(len(three)):
      if thirdatomB[a]==three[i]:
       thirdatomB2.append(three2[i])
       firstatomB2.append(dataatomB[0])
       secondatomB2.append(dataatomB[1])
     
       fourthatomB2.append(dataatomB[3])
       fifthdatomB2.append(dataatomB[4])
       sixthatomB2.append(dataatomB[5])
       seventhhatomB2.append(dataatomB[6])
       eightthatomB2.append(dataatomB[7])

print(thirdatomB)
p=0
with open("newligandA.txt") as fA:
    with open("hybridpdb.txt", "w") as fpdb:
        lines=fA.readlines()
        for i in range(0,len(lines)):
         line=lines[i]
         p=p+1
         fpdb.write(line)
           #else:
        for i in range(len(secondatomB2)):
                   fpdb.write("%4s" %(firstatomB2[i]))
                   fpdb.write("%7s" %(p+i))
                   fpdb.write("%5s" %(thirdatomB2[i]))
                   fpdb.write("%4s" %(fourthatomB2[i]))
                   fpdb.write("%6s" %(fifthdatomB2[i]))
                   fpdb.write("%12s" %(sixthatomB2[i]))
                   fpdb.write("%8s" %(seventhhatomB2[i]))
                   fpdb.write("%8s\n" %(eightthatomB2[i]))
                   
#####################################################################################################################
#####################################   PRM UPDATE  #################################################################
#####################################################################################################################

ligandAprm = open('newligandBprm.txt','r')   ####ALLAZEIS EDW!!!!!!!!!!!!!

prm=[];firstprm=[];secondprm=[];thirdprm=[];fourthprm=[];fifthprm=[];sixthprm=[];seventhprm=[];
eightthprm=[];ninethprm=[];tenthprm=[];eleprm=[];twprm=[];thirprm=[];fortprm=[];fiprm=[]

num_lines = sum(1 for line in open('newligandBprm.txt'))  ####ALLAZEIS EDW!!!!!!!!!!!!!
print (num_lines)
for i in range(num_lines):

    line1prm = ligandAprm.readline().strip()
    prm.append(line1prm)

    dataprm = prm[i]
    dataprm = dataprm.split()
    
    le=len(dataprm)
    #print(le)
    if le == 0:
     firstprm.append('')
     secondprm.append('')
     thirdprm.append('')
     fourthprm.append('')
     fifthprm.append('')
     sixthprm.append('')
     seventhprm.append('')
     eightthprm.append('')
     ninethprm.append('')
     tenthprm.append('')
     eleprm.append('')
     twprm.append('')
     thirprm.append('')
     fortprm.append('')
     fiprm.append('')
    for j in range(le):
     if j==0:
      firstprm.append(dataprm[j])
      if le<=1:
       secondprm.append('')
       thirdprm.append('')
       fourthprm.append('')
       fifthprm.append('')
       sixthprm.append('')
       seventhprm.append('')
       eightthprm.append('')
       ninethprm.append('')
       tenthprm.append('')
       eleprm.append('')
       twprm.append('')
       thirprm.append('')
       fortprm.append('')
       fiprm.append('')
     if j==1:
      secondprm.append(dataprm[j])
      if le<=2:
       thirdprm.append('')
       fourthprm.append('')
       fifthprm.append('')
       sixthprm.append('')
       seventhprm.append('')
       eightthprm.append('')
       ninethprm.append('')
       tenthprm.append('')
       eleprm.append('')
       twprm.append('')
       thirprm.append('')
       fortprm.append('')
       fiprm.append('')
     if j==2:
      thirdprm.append(dataprm[j])
      if le<=3:
       fourthprm.append('')
       fifthprm.append('')
       sixthprm.append('')
       seventhprm.append('')
       eightthprm.append('')
       ninethprm.append('')
       tenthprm.append('')
       eleprm.append('')
       twprm.append('')
       thirprm.append('')
       fortprm.append('')
       fiprm.append('')
     if j==3:
      fourthprm.append(dataprm[j])
      if le<=4:
       fifthprm.append('')
       sixthprm.append('')
       seventhprm.append('')
       eightthprm.append('')
       ninethprm.append('')
       tenthprm.append('')
       eleprm.append('')
       twprm.append('')
       thirprm.append('')
       fortprm.append('')
       fiprm.append('')
     if j==4:
      fifthprm.append(dataprm[j])
      if le<=5:
       sixthprm.append('')
       seventhprm.append('')
       eightthprm.append('')
       ninethprm.append('')
       tenthprm.append('')
       eleprm.append('')
       twprm.append('')
       thirprm.append('')
       fortprm.append('')
       fiprm.append('')
     if j==5:
      sixthprm.append(dataprm[j])
      if le<=6:
       seventhprm.append('')
       eightthprm.append('')
       ninethprm.append('')
       tenthprm.append('')
       eleprm.append('')
       twprm.append('')
       thirprm.append('')
       fortprm.append('')
       fiprm.append('')
     if j==6:
      seventhprm.append(dataprm[j])
      if le<=7:
       eightthprm.append('')
       ninethprm.append('')
       tenthprm.append('')
       eleprm.append('')
       twprm.append('')
       thirprm.append('')
       fortprm.append('')
       fiprm.append('')
     if j==7:
      eightthprm.append(dataprm[j])
      if le<=8:
       ninethprm.append('')
       tenthprm.append('')
       eleprm.append('')
       twprm.append('')
       thirprm.append('')
       fortprm.append('')
       fiprm.append('')
     if j==8:
      ninethprm.append(dataprm[j])
      if le<=9:
       tenthprm.append('')
       eleprm.append('')
       twprm.append('')
       thirprm.append('')
       fortprm.append('')
       fiprm.append('')
     if j==9:
      tenthprm.append(dataprm[j])
      if le<=10:
       eleprm.append('')
       twprm.append('')
       thirprm.append('')
       fortprm.append('')
       fiprm.append('')
     if j==10:
      eleprm.append(dataprm[j])
      if le<=11:
       twprm.append('')
       thirprm.append('')
       fortprm.append('')
       fiprm.append('')
     if j==11:
      twprm.append(dataprm[j])
      if le<=12:
       thirprm.append('')
       fortprm.append('')
       fiprm.append('')
     if j==12:
      thirprm.append(dataprm[j])
      if le<=13:
       fortprm.append('')
       fiprm.append('')
     if j==13:
      fortprm.append(dataprm[j])
      if le<=14:
       fiprm.append('')
     if j==14:
       fiprm.append(dataprm[j])

for i in range(len(firstprm)):
 for j in range(len(four)):
   if firstprm[i]==four[j]:
      #print("psit")
      firstprm[i]=four2[j]

for i in range(len(secondprm)):
 for j in range(len(four)):
   if secondprm[i]==four[j]:
      secondprm[i]=four2[j]

for i in range(len(thirdprm)):
 for j in range(len(four)):
   if thirdprm[i]==four[j]:
      thirdprm[i]=four2[j]

for i in range(len(fourthprm)):
 for j in range(len(three)):
   if fourthprm[i]==four[j]:
      fourthprm[i]=four2[j]
newprm= open('updatedprm.txt','w+')  ###THA EINAI NEO ARXEIO PRM

for i in range(num_lines):
    if firstprm[i]=='X':
      newprm.write("%s    " %(firstprm[i]))
      newprm.write("%s    " %(secondprm[i]))
      newprm.write("%s    " %(thirdprm[i]))
      newprm.write("%s    " %(fourthprm[i]))
      newprm.write("%s " %(fifthprm[i]))
      newprm.write("%s " %(sixthprm[i]))
      newprm.write("%s " %(seventhprm[i]))
      newprm.write("%s " %(eightthprm[i]))
      newprm.write("%s " %(ninethprm[i]))
      newprm.write("%s " %(tenthprm[i]))
      newprm.write("%s " %(eleprm[i]))
      newprm.write("%s " %(twprm[i]))
      newprm.write("%s " %(thirprm[i]))
      newprm.write("%s " %(fortprm[i]))
      newprm.write("%s \n" %(fiprm[i]))
    else:
      newprm.write("%s " %(firstprm[i]))
      newprm.write("%s " %(secondprm[i]))
      newprm.write("%s " %(thirdprm[i]))
      newprm.write("%s " %(fourthprm[i]))
      newprm.write("%s " %(fifthprm[i]))
      newprm.write("%s " %(sixthprm[i]))
      newprm.write("%s " %(seventhprm[i]))
      newprm.write("%s " %(eightthprm[i]))
      newprm.write("%s " %(ninethprm[i]))
      newprm.write("%s " %(tenthprm[i]))
      newprm.write("%s " %(eleprm[i]))
      newprm.write("%s " %(twprm[i]))
      newprm.write("%s " %(thirprm[i]))
      newprm.write("%s " %(fortprm[i]))
      newprm.write("%s \n" %(fiprm[i]))

newprm.close()
#################################################################################
######################## REMOVE DUPLICATES ######################################
#################################################################################
lines_seen = set() # holds lines already seen
outfile = open("final.txt", "w")
for line in open("f.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()   
