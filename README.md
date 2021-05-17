# FEPrepare is NOT available as a stand alone program! To use FEPrepare please use [FEPrepare](https://feprepare.vi-seem.eu/) web-server


# FEPrepare

FEP prepare automates the set-up procedure for performing NAMD/FEP simulations. 

## Pre-requirements

Install [VMD](https://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD)

Align your ligands and protein

## The code used in FEPrepare is described below.

a) `names3.py` ensures consistency between the atoms of the ligands and it creates the following files: newligandA.txt, newligandB.txt, newligandArtf.txt, newligandBrtf.txt, newligandAprm.txt, newligandBprm.txt, how_many.

b) `merge2.py` identifies the common atoms between reference and mutant ligands. It returns sortedB, which is the .rtf file of the mutant ligand sorted          according to the reference ligand.

c) `dual2.py` implements the dual topology methodology. It generates files where both ligands coexist (pdb: hybridpdb.txt, rtf: final.txt, prm: updated.prm)

d) `complex.py` generates a complex file where the hybrid ligand generated above and the protein coexist.

e) `split_chains.py` generates the psfgen file needed from VMD.

### VMD commands:

f) `vmd -dispdev text -e psfgen`


g) if you would you like to add 150μΜ NaCl to your system:

`vmd -dispdev text -e vmd_prepare_complex_after_gui_autopsf_ionize > vmd_log.txt`
        
   otherwise:
   
`vmd -dispdev text -e vmd_prepare_complex_after_gui_autopsf > vmd_log.txt`

h) `vmd -dispdev text -e psfgen_solv`

i) if you would you like to add 150μΜ NaCl to your system:

`vmd -dispdev text -e vmd_prepare_ligand_after_gui_autopsf_ionize > vmd_log.txt`
   
   otherwise:
   
`vmd -dispdev text -e vmd_prepare_ligand_after_gui_autopsf > vmd_log.txt`

j) `fep.py` generated the necessary ionized_fep files for the simulation.

k) `min-max.py` returns the coordinates of the center of the box.
