# FEPrepare
FEP prepare automates the set-up procedure for performing NAMD/FEP simulations. 

Prerequirements 
Instal [VMD] (https://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD)
Align your ligands and protein

To execute the code follow the steps described below.

a) python names3.py /path/to/reference.pdb /path/to/mutant.pdb /path/to/reference.rtf /path/to/mutant.rtf /path/to/reference.prm /path/to/mutant.prm
    This script ensures consistency between the atoms of the ligands and it creates the following files: newligandA.txt, newligandB.txt, newligandArtf.txt, newligandBrtf.txt, newligandAprm.txt, newligandBprm.txt, how_many.

b) python merge2.py newligandArtf.txt newligandBrtf.txt > sortedB
    This script identifies the common atoms between reference and mutant ligands. It returns sortedB, which is the .rtf file of the mutant ligand sorted          according to the reference ligand.

c) python dual2.py 
    This script implements the dual topology methodology. It generates files where both ligands coexist (pdb: hybridpdb.txt, rtf: final.txt, prm: updated.prm)

d) python complex.py /path/to/protein.pdb
    This script generates a complex file where the hybrid ligand generated above and the protein coexist.

e) python split_chains.py complex newligandA.txt
    This script generates the psfgen file needed from VMD.

VMD commands:
f) run_vmd_tmp -dispdev text -e psfgen

g) if you would you like to add 150μΜ NaCl to your system:
        run_vmd_tmp -dispdev text -e vmd_prepare_complex_after_gui_autopsf_ionize > vmd_log.txt
   otherwise:
       run_vmd_tmp -dispdev text -e vmd_prepare_complex_after_gui_autopsf > vmd_log.txt

h) run_vmd_tmp -dispdev text -e psfgen_solv

i) if you would you like to add 150μΜ NaCl to your system:
        run_vmd_tmp -dispdev text -e vmd_prepare_ligand_after_gui_autopsf_ionize > vmd_log.txt
   otherwise:
        run_vmd_tmp -dispdev text -e vmd_prepare_ligand_after_gui_autopsf > vmd_log.txt 

j) python fep.py path/to/complex/ionized.fep path/to/solvent/ionized.fep path/to/complex/ionized.pdb path/to/solvent/ionized.pdb
   This script generated the necessary ionized_fep files for the simulation.

k) min-max.py complex/vmd_log.txt solvent/vmd_log.txt
   This script returns the coordinates of the center of the box.
