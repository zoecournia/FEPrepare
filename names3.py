#Changing atoms names
#Stamatia Zavitsanou
#to execute type in command line python names.py

################################################################################
################## CHANGING THE ATOM NAMES IN THE PDB FILE######################
################################################################################
import sys
import os
import difflib
import string
print("Starting with the pdbs!")
####for the reference ligand#############
fileA = sys.argv[1]
fileB = sys.argv[2]
fileC = sys.argv[3]
fileD = sys.argv[4]
fileE = sys.argv[5]
fileF = sys.argv[6]

#ligandA = open('ck666.pdb','r')
#ligandB = open('ai065.pdb','r')

new= open('newligandA.txt','w+')
newmut= open('newligandB.txt','w+')

atom_lines1=0;atom_lines2=0;
atom1=[];atom2=[];
with open(fileA) as ligandA:
 with open(fileB) as ligandB:
  while True:
# check only the lines that begin with atom
#we read both files and keep the ATOMs

    line1 = ligandA.readline().strip()
    if line1.startswith('ATOM'): 
        atom_lines1=atom_lines1+1
        atom1.append(line1)

    line2 = ligandB.readline().strip()
    if line2.startswith('ATOM'):
        atom_lines2=atom_lines2+1
        atom2.append(line2)

    if line1.startswith('TER') and line2.startswith('TER'):
        break;
    if line1 == '' and line2 == '':
        break;
########################
typos=[];number=[];name=[];lig=[];kati=[];x=[];y=[];z=[]

for i in range(atom_lines1):
    atomdata = atom1[i]
    atomdata = atomdata.split()
    
    typos.append(atomdata[0])
    number.append(atomdata[1])
    name.append(atomdata[2])
    lig.append(atomdata[3])
    kati.append(atomdata[4])
    x.append(atomdata[5])
    y.append(atomdata[6])
    z.append(atomdata[7])

########################
typos2=[];number2=[];name2=[];lig2=[];kati2=[];x2=[];y2=[];z2=[]
mutation=[];mut=[];muttypos=[];mutnumber=[];mutname=[];mutlig=[];mutkati=[];mutx=[];muty=[];mutz=[]
refx=[];refy=[];refz=[];diffmname=[];diffrname=[];
xm=[];ym=[];zm=[];xr=[];yr=[];zr=[];namem=[];namer=[]
namemut2=[]
u=0;
for j in range(atom_lines2):
    atomdata2 = atom2[j]
    atomdata2 = atomdata2.split()
    
    typos2.append(atomdata2[0])
    number2.append(atomdata2[1])
    name2.append(atomdata2[2])
    namemut2.append(atomdata2[2])
    lig2.append(atomdata2[3])
    kati2.append(atomdata2[4])
    x2.append(atomdata2[5])
    y2.append(atomdata2[6])
    z2.append(atomdata2[7])
    if name2[j] not in name:     #the difference in the mutation is somewhere here so we keep it
      print(name2[j])       
      mutname.append(name2[j])
drefx=[];drefy=[];drefz=[];drefname=[];dmutx=[];dmuty=[];dmutz=[];dmutname=[]
print(namemut2)

######the mutation has more than 1 unit difference in two of the three axes####
###############################################################################
for i in range(min(len(x), len(x2))):
     refx = float(x[i])
     mutx = float(x2[i])
     refy = float(y[i])
     muty = float(y2[i])
     refz = float(z[i])
     mutz = float(z2[i])
     nameref = name[i]
     namemut = name2[i]
     if (((refx-mutx)<1 or (mutx-refx)<1) and ((refy-muty)<1 or (muty-refy)<1) and ((refz-mutz)<1 or (mutz-refz)<1)):
        print(refx,mutx)   #for these we have to change the names to aligne to the correct xyz
        drefx.append(refx)  #these are the xyz of the reference
        drefy.append(refy)
        drefz.append(refz)
        drefname.append(nameref)

        dmutx.append(mutx)  #these are the xyz of the mutant that have to match to the reference
        dmuty.append(muty)
        dmutz.append(mutz)
        dmutname.append(namemut) 
     else:
        print(nameref,namemut)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print (drefname,dmutname)
mut=[]
dmut2x=[];dref2x=[];dmut2y=[];dmut2z=[];dref2y=[];dref2z=[];drefname2=[];dmutname2=[]
drn2=[];dmn2=[]
for i in range(len(drefx)): 
   for j in range(len(dmutx)):
         pmut=dmutname[j].strip()
         pref=drefname[i].strip()
         am=pmut[0]
         bm=pmut[1]
         cm=pmut[2]
         ar=pref[0]
         br=pref[1]
         cr=pref[2]
         if am==ar:###the names have to be the same to match,it cant be a different name
          
          if ((abs(dmutx[j]-drefx[i])<0.5) and (abs(dmuty[j]-drefy[i])<0.5) and (abs(dmutz[j]-drefz[i])<0.5)):  
                dmut2x.append(dmutx[j])
                dref2x.append(drefx[i])
                dmut2y.append(dmuty[j])
                dref2y.append(drefy[i])
                dmut2z.append(dmutz[j])
                dref2z.append(drefz[i])
                drefname2.append(drefname[i]) #and the names
                dmutname2.append(dmutname[j])
                print (dmutname[j],drefname[i])
                print (dmutx[j],drefx[i]) 
                break;
          
          
         else: ###which mutation matches which reference atom
           if ((abs(dmutx[j]-drefx[i])<0.5) and (abs(dmuty[j]-drefy[i])<0.5) and (abs(dmutz[j]-drefz[i])<0.5)):
                drn2.append(drefname[i]) 
                dmn2.append(dmutname[j])
                print (dmutname[j],drefname[i])
                print ("mpike")

print("\n")
print("\n")
print(drn2,dmn2)####pair of mutations
print("\n")
print("\n")
print (dmut2x,dmutname2)  #there are kept in pairs as they should change
print (dref2x,drefname2) 
print("\n")
print("\n")
#print (namer,namem)
mut=[];mx2=[];mx2str=[]
print mutname
#for i in range(len(mutname)):
 #if mutname[i] not in dmutname2:
  #  mut.append(mutname[i])
#print(mut)        ####This is the mutation after all!!!!!!!!!!!!

print("*******************************************")
###############################################################
####we rename the reference ligand for the pdb################
###############################################################
newname=[];a=[];b=[];c=[];what=[];mylist=[];m=0;mi=[];mi2=[];mh=[[],[],[]];mh2=[[],[]];bisalphalist=[];aisalphalist=[];
f2=[];f=[]
for i in range(atom_lines1):
  newname=[None] * atom_lines1
for i in range(atom_lines1):
    parts=name[i].strip()
    a=parts[0]
    b=parts[1]
    c=parts[2]
    
    if b.isalpha():
        bisalphalist.append(a+b)    
        how_many2=([[ww,bisalphalist.count(ww)] for ww in set(bisalphalist)])
        f2.append(int(i))
    else:
        mylist.append(a)
        how_many=([[w,mylist.count(w)] for w in set(mylist)])
        f.append(int(i))
print f2
if len(f2)!=0:
 for jj in range(len(how_many2)):
         mh2[0].append(how_many2[jj][0])
         mh2[1].append(int(0))
         mi2.append(how_many2[jj][1])

 for i in range(len(bisalphalist)):
  for j in range(len(mh2[0])):
      if bisalphalist[i]==mh2[0][j]:
         ola=[mh2[0][j],mh2[1][j]]
         mh2[1][j]=mh2[1][j]+1
         print(ola)
         print f2[i]
         ff=f2[i]
         newname[ff]=(str(ola))
         print(newname)
if len(f)!=0:
 for j in range(len(how_many)):
         mh[0].append(how_many[j][0])
         mh[1].append(int(0))
         mh[2].append(int(0))
         mi.append(how_many[j][1])
 print mh
 for i in range(len(mylist)):
  for j in range(len(mh[0])):
      if mylist[i]==mh[0][j]:
         ola=[mh[0][j],mh[1][j],mh[2][j]]
         mh[2][j]=mh[2][j]+1
         if mh[2][j]>9:
           mh[1][j]=mh[1][j]+1
           mh[2][j]=0
         print(ola)
         print (f[i])
         fff=f[i]
         newname[fff]=(str(ola))
         print(newname)
for i in range (len(newname)):
 print len(newname[i])
 if len(newname[i])==9:
  newname[i]=newname[i][2]+newname[i][3]+newname[i][7]
 else:
  newname[i]=newname[i][2]+newname[i][6]+newname[i][9]
print(newname)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
print(mylist)
print(how_many)
with open('how_many', 'w') as outfile:  
  outfile.write("%s"%(how_many))  
  if len(f2)!=0:         
   outfile.write("%s"%(how_many2))      
new.write("REMARK LIGPARGEN GENERATED PDB FILE\n")
for i in range(atom_lines1):
    new.write("%4s" %(typos[i]))
    new.write("%7s" %(number[i]))  
    new.write("%5s" %(newname[i]))    
    new.write("%4s" %(lig[i]))    
    new.write("%6s" %(kati[i]))   
    new.write("%12s" %(x[i]))    
    new.write("%8s" %(y[i]))   
    new.write("%8s\n" %(z[i]))
new.close()

####so far the reference ligand has new names

####now we have to give the correct names to the mutant ligand according to the x,y,z


new= open('newligandA.txt','r+')
atom_lines1_new=0;
atom1_new=[];

#so now for the newnamed reference we do the same

while True:
    line1_new = new.readline().strip()
    if line1_new.startswith('ATOM'): 
        atom_lines1_new=atom_lines1_new+1
        atom1_new.append(line1_new)

    if line1_new.startswith('TER'):
        break;
    if line1_new == '' :
        break;
diffrefx=[];diffref2x=[];diffrefname2=[];diffrefname=[];diffrefy=[];diffrefz=[];diffref2y=[];diffref2z=[];
diffmutx=[];diffmut2x=[];diffmutname=[];diffmutname2=[];diffmuty=[];diffmutz=[];diffmut2y=[];diffmut2z=[];
####for the new reference#########
typos_new=[];number_new=[];name_new=[];lig_new=[];kati_new=[];x_new=[];y_new=[];z_new=[]
for i in range(atom_lines1_new):
    atomdata_new = atom1_new[i]
    atomdata_new = atomdata_new.split()
    
    typos_new.append(atomdata_new[0])
    number_new.append(atomdata_new[1])
    name_new.append(atomdata_new[2])
    lig_new.append(atomdata_new[3])
    kati_new.append(atomdata_new[4])
    x_new.append(atomdata_new[5])
    y_new.append(atomdata_new[6])
    z_new.append(atomdata_new[7])
##################################################################################
####let's give correct names to rtf too(before we finish with the pdb of the mutant)
###################################################################################

#ligandrtf = open('ck666.rtf','r')
atom_lines1rtf=0;
mass=[];bond=[];impr=[];atom1rtf=[];
masssum=0;bondsum=0;imprsum=0;
with open(fileC) as ligandrtf:
 while True:
    line1rtf = ligandrtf.readline().strip()
    if line1rtf.startswith('ATOM'): 
        atom_lines1rtf=atom_lines1rtf+1
        atom1rtf.append(line1rtf)
    if line1rtf.startswith('RESI'):
        resi = line1rtf
    if line1rtf.startswith('MASS'):
        masssum=masssum+1
        mass.append(line1rtf)
    if line1rtf.startswith('BOND'):
        bondsum=bondsum+1
        bond.append(line1rtf)
    if line1rtf.startswith('IMPR'):
        imprsum=imprsum+1
        impr.append(line1rtf)
    if line1rtf == '':
        break;
firstatom=[];secondatom=[];thirdatom=[];fourthatom=[]
firstmass=[];secondmass=[];thirdmass=[];fourthmass=[];fifthmass=[]
firstbond=[];secondbond=[];thirdbond=[]
firstimpr=[];secondimpr=[];thirdimpr=[];fourthimpr=[];fifthimpr=[]
atrtf=[];btrtf=[];ctrtf=[];dtrtf=[];etrtf=[]
asrtf=[];bsrtf=[];csrtf=[];
thirdatoma=[]
for a in range(atom_lines1rtf):
    dataatom = atom1rtf[a]
    dataatom = dataatom.split()

    firstatom.append(dataatom[0])
    secondatom.append(dataatom[1])
    thirdatom.append(dataatom[2])
    thirdatoma.append(dataatom[2])
    fourthatom.append(dataatom[3])

for m in range(masssum):
    datamass = mass[m]
    datamass = datamass.split()
    
    firstmass.append(datamass[0])
    secondmass.append(datamass[1])
    thirdmass.append(datamass[2])
    fourthmass.append(datamass[3])
    fifthmass.append(datamass[4])

for b in range (bondsum):
    databond = bond[b]
    databond = databond.split()

    firstbond.append(databond[0])
    secondbond.append(databond[1])
    thirdbond.append(databond[2])

for im in range (imprsum):
    dataimpr = impr[im]
    dataimpr = dataimpr.split()

    firstimpr.append(dataimpr[0])
    secondimpr.append(dataimpr[1])
    thirdimpr.append(dataimpr[2])
    fourthimpr.append(dataimpr[3])
    fifthimpr.append(dataimpr[4])

for i in range(atom_lines1rtf):
    if name[i]==secondatom[i]:
        secondatom[i]=name_new[i]
        #print("edw???")
    else:
        print("nai kalaaaaa")
    psrtf=secondatom[i].strip()
    asrtf=psrtf[0]
    bsrtf=psrtf[1]
    csrtf=psrtf[2]
    ptrtf=thirdatom[i].strip()
    atrtf=ptrtf[0]
    btrtf=ptrtf[1]
    #ctrtf=ptrtf[2]
    #dtrtf=ptrtf[3]
    #etrtf=ptrtf[4]
    if btrtf.isalpha():
        fourchar=[atrtf,btrtf,'5',csrtf]
        newthird=''.join(fourchar)
        thirdatom[i]=newthird
    else:
        fourchar=[atrtf,'5',bsrtf,csrtf]
        newthird=''.join(fourchar)
        thirdatom[i]=newthird

for i in range(masssum):
    thirdmass[i]=thirdatom[i]
    
tbond,sbond=[],[]
simpr,timpr,fimpr,fifimpr=[],[],[],[]
for i in range (bondsum):
   for k in range(len(name_new)):
    if secondbond[i]==name[k]:
        sbond.append(name_new[k])
    if thirdbond[i]==name[k]:
        tbond.append(name_new[k])
for i in range(imprsum):
   for k in range(len(name_new)):
    if secondimpr[i]==name[k]:
        simpr.append(name_new[k])
    if thirdimpr[i]==name[k]:
        timpr.append(name_new[k])
    if fourthimpr[i]==name[k]:
        fimpr.append(name_new[k])
    if fifthimpr[i]==name[k]:
        fifimpr.append(name_new[k])

print("lllllllllllllllllllllllll")
print(secondatom)
print(thirdatom)
print(name)
print(sbond)
print(tbond)
print(name_new)
print("lllllllllllllllllllllllll")
newrtf= open('newligandArtf.txt','w+')

newrtf.write("! LigParGen generated RFT file for NAMD/CHARMM \n")
for i in range(masssum):
    newrtf.write("%s " %(firstmass[i]))
    newrtf.write("%s " %(secondmass[i]))
    newrtf.write("%s " %(thirdmass[i]))
    newrtf.write("%s " %(fourthmass[i]))
    newrtf.write("%s\n" %(fifthmass[i]))
newrtf.write("AUTO ANGLES DIHE \n")
newrtf.write("%s \n" %resi)
for i in range(atom_lines1rtf):
    newrtf.write("%s " %(firstatom[i]))
    newrtf.write("%s " %(secondatom[i]))
    newrtf.write("%s " %(thirdatom[i]))
    newrtf.write("%s\n" %(fourthatom[i]))
for i in range(bondsum):
    newrtf.write("%s " %(firstbond[i]))
    newrtf.write("%s " %(sbond[i]))
    newrtf.write("%s\n" %(tbond[i]))
for i in range(imprsum):
    newrtf.write("%s " %(firstimpr[i]))
    newrtf.write("%s " %(simpr[i]))
    newrtf.write("%s " %(timpr[i]))
    newrtf.write("%s " %(fimpr[i]))
    newrtf.write("%s\n" %(fifimpr[i]))
newrtf.write("PATCH FIRST NONE LAST NONE\n")
newrtf.write("END \n")
newrtf.close()
#################################################################################################
##########done with rtf names continueing what we were doing with the renaming of the mutant pdb
###################################################################################################
if len(x)>len(x2):
  diff=len(x)-len(x2)
  print diff
  for i in range(diff):
   diffnew=diff-i
   print(x[-diffnew])

   diffrefname.append(name_new[-diffnew])
   diffrefx.append(float(x_new[-diffnew]))
   diffrefy.append(float(y_new[-diffnew]))
   diffrefz.append(float(z_new[-diffnew]))
   
if len(x)<len(x2):
  diff=len(x2)-len(x)
  print diff
  for i in range(diff):
   diffnew=diff-i
   print(x2[-diffnew],y2[-diffnew],z2[-diffnew]) 
   
   diffmutname.append(name2[-diffnew])
   diffmutx.append(float(x2[-diffnew]))
   diffmuty.append(float(y2[-diffnew]))
   diffmutz.append(float(z2[-diffnew]))
                
   print(name2[-diffnew])

mored=list(string.ascii_uppercase)
print mored
j=0
for k in range(len(x2)):
  item2 = float(x2[k])
  item22 = float(y2[k])
  item222 = float(z2[k])
  name22 = name2[k]
  ext=name2[k].strip()
  exta=ext[0]
  flag = 0; 
  for i in range(len(x)):  #difference in axes
    item1 = float(x_new[i])
    item11 = float(y_new[i])
    item111 = float(z_new[i])
    name11 = name_new[i]
    ext2=name_new[i].strip()
    ext2a=ext2[0]
    if ((item1-item2)<0.5 and (item2-item1)<0.5) and ((item11-item22)<0.5 and (item22-item11)<0.5) and ((item111-item222)<0.5 and (item222-item111)<0.5):
     if ext2a==exta:
      name2[k]=name_new[i]
      print name2[k],name_new[i]
      flag = 1
     # break

  if (flag == 0):
      more=name2[k].strip()
      morea=more[0]
      moreb=more[1]
      morec=more[2]
      al=[morea,moreb,mored[j]]
      newt2=''.join(al)
#diffmutname[j]=newt2
      print j
      j=j+1
      name2[k]=newt2
print("############################################")
print diffmutname
print diffrefname

#for i in range (len(diffmutname)):
 # if diffmutname[i] in name_new:
  # for j in range(len(name2)):
   # if diffmutname[i]==name2[j]:
  #    more=diffmutname[i].strip()
   #   morea=more[0]
    #  moreb=more[1]
     # morec=more[2]
      #al=[morea,moreb,mored[i]]
      #newt2=''.join(al)
      #diffmutname[i]=newt2
      #name2[j]=newt2

print("????????????????????????????????")
print (name2)
print (diffmut2x,diffmutname2)  #there are kept in pairs as they should change
print (diffref2x,diffrefname2)
####renaming of the mutant pdb
newmut.write("REMARK LIGPARGEN GENERATED PDB FILE\n")
for i in range(len(name2)):

            newmut.write("%4s" %(typos2[i]))
            newmut.write("%7s" %(number2[i]))
            newmut.write("%5s" %(name2[i]))
            newmut.write("%4s" %(lig2[i]))
            newmut.write("%6s" %(kati2[i]))
            newmut.write("%12s" %(x2[i]))
            newmut.write("%8s" %(y2[i]))
            newmut.write("%8s\n" %(z2[i]))
newmut.close()
######################################################################################################
############## RENAMING THE MUTANT RTF##################################################
#####################################################################################################
newB= open('newligandB.txt','r+')
atom_lines2_new=0;
atom2_new=[];

#so now for the newnamed mutant we do the same

while True:
    line2_new = newB.readline().strip()
    if line2_new.startswith('ATOM'): 
        atom_lines2_new=atom_lines2_new+1
        atom2_new.append(line2_new)

    if line2_new.startswith('TER'):
        break;
    if line2_new == '' :
        break;
####for the new mutatant#########
typos_new2=[];number_new2=[];name_new2=[];lig_new2=[];kati_new2=[];x_new2=[];y_new2=[];z_new2=[]
for i in range(atom_lines2_new):
    atomdata_new2 = atom2_new[i]
    atomdata_new2 = atomdata_new2.split()
    
    typos_new2.append(atomdata_new2[0])
    number_new2.append(atomdata_new2[1])
    name_new2.append(atomdata_new2[2])
    lig_new2.append(atomdata_new2[3])
    kati_new2.append(atomdata_new2[4])
    x_new2.append(atomdata_new2[5])
    y_new2.append(atomdata_new2[6])
    z_new2.append(atomdata_new2[7])

#ligandBrtf = open('ai065.rtf','r')
atom_lines2rtf=0;
mass2=[];bond2=[];impr2=[];atom2rtf=[];
masssum2=0;bondsum2=0;imprsum2=0;

with open(fileD) as ligandBrtf:
 while True:

    line2rtf = ligandBrtf.readline().strip()
    if line2rtf.startswith('ATOM'): 
        atom_lines2rtf=atom_lines2rtf+1
        atom2rtf.append(line2rtf)
    if line2rtf.startswith('RESI'):
       resi2 = line2rtf
    if line2rtf.startswith('MASS'):
        masssum2=masssum2+1
        mass2.append(line2rtf)
    if line2rtf.startswith('BOND'):
        bondsum2=bondsum2+1
        bond2.append(line2rtf)
    if line2rtf.startswith('IMPR'):
        imprsum2=imprsum2+1
        impr2.append(line2rtf)
    if line2rtf == '':
        break;
firstatom2=[];secondatom2=[];thirdatom2=[];fourthatom2=[]
firstmass2=[];secondmass2=[];thirdmass2=[];fourthmass2=[];fifthmass2=[]
firstbond2=[];secondbond2=[];thirdbond2=[]
firstimpr2=[];secondimpr2=[];thirdimpr2=[];fourthimpr2=[];fifthimpr2=[]
atrtf2=[];btrtf2=[];ctrtf2=[];dtrtf2=[];etrtf2=[]
asrtf2=[];bsrtf2=[];csrtf2=[];
thirdatom2a=[]
for a in range(atom_lines2rtf):
    dataatom2 = atom2rtf[a]
    dataatom2 = dataatom2.split()

    firstatom2.append(dataatom2[0])
    secondatom2.append(dataatom2[1])
    thirdatom2.append(dataatom2[2])
    thirdatom2a.append(dataatom2[2])
    fourthatom2.append(dataatom2[3])

for m in range(masssum2):
    datamass2 = mass2[m]
    datamass2 = datamass2.split()
    
    firstmass2.append(datamass2[0])
    secondmass2.append(datamass2[1])
    thirdmass2.append(datamass2[2])
    fourthmass2.append(datamass2[3])
    fifthmass2.append(datamass2[4])

for b in range (bondsum2):
    databond2 = bond2[b]
    databond2 = databond2.split()

    firstbond2.append(databond2[0])
    secondbond2.append(databond2[1])
    thirdbond2.append(databond2[2])

for im in range (imprsum2):
    dataimpr2 = impr2[im]
    dataimpr2 = dataimpr2.split()

    firstimpr2.append(dataimpr2[0])
    secondimpr2.append(dataimpr2[1])
    thirdimpr2.append(dataimpr2[2])
    fourthimpr2.append(dataimpr2[3])
    fifthimpr2.append(dataimpr2[4])
print("~~~~~~~~~~~~~~~~")
print (name_new2)
print(namemut2)
print("~~~~~~~~~~~~~~~~")
for i in range(atom_lines2rtf):
    if namemut2[i]==secondatom2[i]:
        secondatom2[i]=name2[i]
        #print("edw???")
    else:
        print("nai kalaaaaa")
    psrtf2=secondatom2[i].strip()
    asrtf2=psrtf2[0]
    bsrtf2=psrtf2[1]
    csrtf2=psrtf2[2]
    ptrtf2=thirdatom2[i].strip()
    atrtf2=ptrtf2[0]
    btrtf2=ptrtf2[1]
    #ctrtf=ptrtf[2]
    #dtrtf=ptrtf[3]
    #etrtf=ptrtf[4]
    if btrtf2.isalpha():
        fourchar2=[atrtf2,btrtf2,'5',csrtf2]
        newthird2=''.join(fourchar2)
        #print(newthird)
        thirdatom2[i]=newthird2
    else:
        fourchar2=[atrtf2,'5',bsrtf2,csrtf2]
        newthird2=''.join(fourchar2)
        #print(newthird)
        thirdatom2[i]=newthird2

for i in range(masssum2):
    thirdmass2[i]=thirdatom2[i]
    
sbond2,tbond2=[],[]
simpr2,timpr2,fimpr2,fifimpr2=[],[],[],[]
for i in range (bondsum2):
   for k in range(len(name_new2)):
    if secondbond2[i]==namemut2[k]:
        sbond2.append(name_new2[k])
    if thirdbond2[i]==namemut2[k]:
        tbond2.append(name_new2[k])
for i in range(imprsum2):
   for k in range(len(name_new2)):
    if secondimpr2[i]==namemut2[k]:
        simpr2.append(name_new2[k])
    if thirdimpr2[i]==namemut2[k]:
        timpr2.append(name_new2[k])
    if fourthimpr2[i]==namemut2[k]:
        fimpr2.append(name_new2[k])
    if fifthimpr2[i]==namemut2[k]:
        fifimpr2.append(name_new2[k])

print("lllllllllllllllllllllllll")
print(secondatom2)
print(thirdatom2)
print(name2)
print(sbond2)
print(tbond2)
print(name_new)
print("lllllllllllllllllllllllll")
newrtfB= open('newligandBrtf.txt','w+')

newrtfB.write("! LigParGen generated RFT file for NAMD/CHARMM \n")
for i in range(masssum2):
    newrtfB.write("%s " %(firstmass2[i]))
    newrtfB.write("%s " %(secondmass2[i]))
    newrtfB.write("%s " %(thirdmass2[i]))
    newrtfB.write("%s " %(fourthmass2[i]))
    newrtfB.write("%s\n" %(fifthmass2[i]))
newrtfB.write("AUTO ANGLES DIHE \n")
newrtfB.write("%s \n" %resi2)
for i in range(atom_lines2rtf):
    newrtfB.write("%s " %(firstatom2[i]))
    newrtfB.write("%s " %(secondatom2[i]))
    newrtfB.write("%s " %(thirdatom2[i]))
    newrtfB.write("%s\n" %(fourthatom2[i]))
for i in range(bondsum2):
    newrtfB.write("%s " %(firstbond2[i]))
    newrtfB.write("%s " %(sbond2[i]))
    newrtfB.write("%s\n" %(tbond2[i]))
for i in range(imprsum2):
    newrtfB.write("%s " %(firstimpr2[i]))
    newrtfB.write("%s " %(simpr2[i]))
    newrtfB.write("%s " %(timpr2[i]))
    newrtfB.write("%s " %(fimpr2[i]))
    newrtfB.write("%s\n" %(fifimpr2[i]))
newrtfB.write("PATCH FIRST NONE LAST NONE\n")
newrtfB.write("END \n")
newrtfB.close()
######################################################################################################
##############DONE RENAMING THE LIGAND RTF##################################################
#####################################################################################################

##############################################################################################
################RENAMING THE REFERENCE PRM###################################################
################################################################################################
#ligandAprm = open('ck666.prm','r')

prm=[];firstprm=[];secondprm=[];thirdprm=[];fourthprm=[];fifthprm=[];sixthprm=[];seventhprm=[];
eightthprm=[];ninethprm=[];tenthprm=[];eleprm=[];twprm=[];thirprm=[];fortprm=[];fiprm=[]
with open(fileE) as ligandAprm:
 num_lines = sum(1 for line in open(fileE))
 print (num_lines)
 for i in range(num_lines):


    line1prm = ligandAprm.readline().strip()
    prm.append(line1prm)

    dataprm = prm[i]
    dataprm = dataprm.split()
    #print(dataprm)
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
#print(firstprm)
#print(len(firstprm))
for i in range(len(firstprm)):
 for j in range(len(thirdatoma)):
   if firstprm[i]==thirdatoma[j]:
      firstprm[i]=thirdatom[j]

for i in range(len(secondprm)):
 for j in range(len(thirdatoma)):
   if secondprm[i]==thirdatoma[j]:
      secondprm[i]=thirdatom[j]

for i in range(len(thirdprm)):
 for j in range(len(thirdatoma)):
   if thirdprm[i]==thirdatoma[j]:
      thirdprm[i]=thirdatom[j]

for i in range(len(fourthprm)):
 for j in range(len(thirdatoma)):
   if fourthprm[i]==thirdatoma[j]:
      fourthprm[i]=thirdatom[j]
#print(firstprm)
newprmA= open('newligandAprm.txt','w+')

for i in range(num_lines):
    if firstprm[i]=='X':
      newprmA.write("%s    " %(firstprm[i]))
      newprmA.write("%s    " %(secondprm[i]))
      newprmA.write("%s    " %(thirdprm[i]))
      newprmA.write("%s    " %(fourthprm[i]))
      newprmA.write("%s " %(fifthprm[i]))
      newprmA.write("%s " %(sixthprm[i]))
      newprmA.write("%s " %(seventhprm[i]))
      newprmA.write("%s " %(eightthprm[i]))
      newprmA.write("%s " %(ninethprm[i]))
      newprmA.write("%s " %(tenthprm[i]))
      newprmA.write("%s " %(eleprm[i]))
      newprmA.write("%s " %(twprm[i]))
      newprmA.write("%s " %(thirprm[i]))
      newprmA.write("%s " %(fortprm[i]))
      newprmA.write("%s \n" %(fiprm[i]))
    else:
      newprmA.write("%s " %(firstprm[i]))
      newprmA.write("%s " %(secondprm[i]))
      newprmA.write("%s " %(thirdprm[i]))
      newprmA.write("%s " %(fourthprm[i]))
      newprmA.write("%s " %(fifthprm[i]))
      newprmA.write("%s " %(sixthprm[i]))
      newprmA.write("%s " %(seventhprm[i]))
      newprmA.write("%s " %(eightthprm[i]))
      newprmA.write("%s " %(ninethprm[i]))
      newprmA.write("%s " %(tenthprm[i]))
      newprmA.write("%s " %(eleprm[i]))
      newprmA.write("%s " %(twprm[i]))
      newprmA.write("%s " %(thirprm[i]))
      newprmA.write("%s " %(fortprm[i]))
      newprmA.write("%s \n" %(fiprm[i]))

newprmA.close()
##############################################################################################
################ DONE RENAMING THE REFERENCE PRM###################################################
################################################################################################
##############################################################################################
################RENAMING THE MUTANT PRM###################################################
################################################################################################
#ligandBprm = open('ai065.prm','r')

prm2=[];firstprm2=[];secondprm2=[];thirdprm2=[];fourthprm2=[];fifthprm2=[];sixthprm2=[];seventhprm2=[];
eightthprm2=[];ninethprm2=[];tenthprm2=[];eleprm2=[];twprm2=[];thirprm2=[];fortprm2=[];fiprm2=[]

with open(fileF) as ligandBprm:
 num_lines2 = sum(1 for line in open(fileF))
 print (num_lines2)
 for i in range(num_lines2):

    line2prm = ligandBprm.readline().strip()
    prm2.append(line2prm)

    dataprm2 = prm2[i]
    dataprm2 = dataprm2.split()
    #print(dataprm2)
    le2=len(dataprm2)
    #print(le2)
    if le2 == 0:
     firstprm2.append('')
     secondprm2.append('')
     thirdprm2.append('')
     fourthprm2.append('')
     fifthprm2.append('')
     sixthprm2.append('')
     seventhprm2.append('')
     eightthprm2.append('')
     ninethprm2.append('')
     tenthprm2.append('')
     eleprm2.append('')
     twprm2.append('')
     thirprm2.append('')
     fortprm2.append('')
     fiprm2.append('')
    for j in range(le2):
     if j==0:
      firstprm2.append(dataprm2[j])
      if le2<=1:
       secondprm2.append('')
       thirdprm2.append('')
       fourthprm2.append('')
       fifthprm2.append('')
       sixthprm2.append('')
       seventhprm2.append('')
       eightthprm2.append('')
       ninethprm2.append('')
       tenthprm2.append('')
       eleprm2.append('')
       twprm2.append('')
       thirprm2.append('')
       fortprm2.append('')
       fiprm2.append('')
     if j==1:
      secondprm2.append(dataprm2[j])
      if le2<=2:
       thirdprm2.append('')
       fourthprm2.append('')
       fifthprm2.append('')
       sixthprm2.append('')
       seventhprm2.append('')
       eightthprm2.append('')
       ninethprm2.append('')
       tenthprm2.append('')
       eleprm2.append('')
       twprm2.append('')
       thirprm2.append('')
       fortprm2.append('')
       fiprm2.append('')
     if j==2:
      thirdprm2.append(dataprm2[j])
      if le2<=3:
       fourthprm2.append('')
       fifthprm2.append('')
       sixthprm2.append('')
       seventhprm2.append('')
       eightthprm2.append('')
       ninethprm2.append('')
       tenthprm2.append('')
       eleprm2.append('')
       twprm2.append('')
       thirprm2.append('')
       fortprm2.append('')
       fiprm2.append('')
     if j==3:
      fourthprm2.append(dataprm2[j])
      if le2<=4:
       fifthprm2.append('')
       sixthprm2.append('')
       seventhprm2.append('')
       eightthprm2.append('')
       ninethprm2.append('')
       tenthprm2.append('')
       eleprm2.append('')
       twprm2.append('')
       thirprm2.append('')
       fortprm2.append('')
       fiprm2.append('')
     if j==4:
      fifthprm2.append(dataprm2[j])
      if le2<=5:
       sixthprm2.append('')
       seventhprm2.append('')
       eightthprm2.append('')
       ninethprm2.append('')
       tenthprm2.append('')
       eleprm2.append('')
       twprm2.append('')
       thirprm2.append('')
       fortprm2.append('')
       fiprm2.append('')
     if j==5:
      sixthprm2.append(dataprm2[j])
      if le2<=6:
       seventhprm2.append('')
       eightthprm2.append('')
       ninethprm2.append('')
       tenthprm2.append('')
       eleprm2.append('')
       twprm2.append('')
       thirprm2.append('')
       fortprm2.append('')
       fiprm2.append('')
     if j==6:
      seventhprm2.append(dataprm2[j])
      if le2<=7:
       eightthprm2.append('')
       ninethprm2.append('')
       tenthprm2.append('')
       eleprm2.append('')
       twprm2.append('')
       thirprm2.append('')
       fortprm2.append('')
       fiprm2.append('')
     if j==7:
      eightthprm2.append(dataprm2[j])
      if le2<=8:
       ninethprm2.append('')
       tenthprm2.append('')
       eleprm2.append('')
       twprm2.append('')
       thirprm2.append('')
       fortprm2.append('')
       fiprm2.append('')
     if j==8:
      ninethprm2.append(dataprm2[j])
      if le2<=9:
       tenthprm2.append('')
       eleprm2.append('')
       twprm2.append('')
       thirprm2.append('')
       fortprm2.append('')
       fiprm2.append('')
     if j==9:
      tenthprm2.append(dataprm2[j])
      if le2<=10:
       eleprm2.append('')
       twprm2.append('')
       thirprm2.append('')
       fortprm2.append('')
       fiprm2.append('')
     if j==10:
      eleprm2.append(dataprm2[j])
      if le2<=11:
       twprm2.append('')
       thirprm2.append('')
       fortprm2.append('')
       fiprm2.append('')
     if j==11:
      twprm2.append(dataprm2[j])
      if le2<=12:
       thirprm2.append('')
       fortprm2.append('')
       fiprm2.append('')
     if j==12:
      thirprm2.append(dataprm2[j])
      if le2<=13:
       fortprm2.append('')
       fiprm2.append('')
     if j==13:
      fortprm2.append(dataprm2[j])
      if le2<=14:
       fiprm2.append('')
     if j==14:
       fiprm2.append(dataprm2[j])
#print(firstprm2)
#print(len(firstprm2))
for i in range(len(firstprm2)):
 for j in range(len(thirdatom2a)):
   if firstprm2[i]==thirdatom2a[j]:
      firstprm2[i]=thirdatom2[j]

for i in range(len(secondprm2)):
 for j in range(len(thirdatom2a)):
   if secondprm2[i]==thirdatom2a[j]:
      secondprm2[i]=thirdatom2[j]

for i in range(len(thirdprm2)):
 for j in range(len(thirdatom2a)):
   if thirdprm2[i]==thirdatom2a[j]:
      thirdprm2[i]=thirdatom2[j]

for i in range(len(fourthprm2)):
 for j in range(len(thirdatom2a)):
   if fourthprm2[i]==thirdatom2a[j]:
      fourthprm2[i]=thirdatom2[j]
#print(firstprm)
newprmB= open('newligandBprm.txt','w+')

for i in range(num_lines2):
    if firstprm2[i]=='X':
      newprmB.write("%s    " %(firstprm2[i]))
      newprmB.write("%s    " %(secondprm2[i]))
      newprmB.write("%s    " %(thirdprm2[i]))
      newprmB.write("%s    " %(fourthprm2[i]))
      newprmB.write("%s " %(fifthprm2[i]))
      newprmB.write("%s " %(sixthprm2[i]))
      newprmB.write("%s " %(seventhprm2[i]))
      newprmB.write("%s " %(eightthprm2[i]))
      newprmB.write("%s " %(ninethprm2[i]))
      newprmB.write("%s " %(tenthprm2[i]))
      newprmB.write("%s " %(eleprm2[i]))
      newprmB.write("%s " %(twprm2[i]))
      newprmB.write("%s " %(thirprm2[i]))
      newprmB.write("%s " %(fortprm2[i]))
      newprmB.write("%s \n" %(fiprm2[i]))
    else:
      newprmB.write("%s " %(firstprm2[i]))
      newprmB.write("%s " %(secondprm2[i]))
      newprmB.write("%s " %(thirdprm2[i]))
      newprmB.write("%s " %(fourthprm2[i]))
      newprmB.write("%s " %(fifthprm2[i]))
      newprmB.write("%s " %(sixthprm2[i]))
      newprmB.write("%s " %(seventhprm2[i]))
      newprmB.write("%s " %(eightthprm2[i]))
      newprmB.write("%s " %(ninethprm2[i]))
      newprmB.write("%s " %(tenthprm2[i]))
      newprmB.write("%s " %(eleprm2[i]))
      newprmB.write("%s " %(twprm2[i]))
      newprmB.write("%s " %(thirprm2[i]))
      newprmB.write("%s " %(fortprm2[i]))
      newprmB.write("%s \n" %(fiprm2[i]))
newprmB.close()
##############################################################################################
################ DONE RENAMING THE REFERENCE PRM###################################################
################################################################################################
ligandAprm.close()
ligandB.close()
ligandA.close()
new.close()
newmut.close()
