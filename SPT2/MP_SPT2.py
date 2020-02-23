#!/usr/bin/env python

from pymatgen import MPRester
from datetime import date

AllElem = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Ac", "Th", "Pa", "U", "Np", "Pu"]
SPT1 = ["Ti", "N", "Al", "Cr", "Mn", "Ge"]
Not_SPT1 = []
for ii in range(0, len(AllElem)):
    if AllElem[ii] in SPT1:
        pass
    else:
        Not_SPT1.append(AllElem[ii])

m = MPRester("2fTJ4oel7nxrzFOd")
data = m.query(criteria=
        {"spacegroup.number":{"$in":[75,76,77,78,79,80,81,82,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,168,169,170,171,172,173,174,177,178,179,180,181,182,183,184,185,186,187,188,189,190,195,196,197,198,207,208,209,210,211,212,213,214,215,216,217,218,219,220]}, 
        "band_gap":0, 
        "magnetic_type":{"$in":["FM","AFM","FiM"]}, 
        "nelements":{"$lte":3}, 
        "elements":{"$in":SPT1}, 
        "elements":{"$nin":Not_SPT1}}, 
        properties=["pretty_formula", "material_id", "formation_energy_per_atom", "unit_cell_formula", "spacegroup", "structure", "magnetic_type", "total_magnetization"], chunk_size=0)

today = date.today()
d = today.strftime("%Y%m%d")

f = open("MP_SPT2_%s.txt" % (d), "w+")

excluded = 0

for ii in range(0, len(data)):
    Ti = data[ii].get('unit_cell_formula').get('Ti')
    N = data[ii].get('unit_cell_formula').get('N')
    Al = data[ii].get('unit_cell_formula').get('Al')
    Cr = data[ii].get('unit_cell_formula').get('Cr')
    Mn = data[ii].get('unit_cell_formula').get('Mn')
    Ge = data[ii].get('unit_cell_formula').get('Ge')
    if data[ii].get("formation_energy_per_atom") < 0:
        if Ti == None and N != None:
            pass
            excluded += 1
        elif (Mn == None and Ge != None) or (Mn != None and Ge == None):
            pass
            excluded += 1
        elif (Ti != None and N != None) and N > Ti:
            pass
            excluded += 1
        elif (Mn != None and Ge != None) and Mn != 2*Ge:
            pass
            excluded += 1
        else:
            pass
    else:
        pass
        excluded += 1



total = len(data) - excluded
f.write("Materials found: %i\n\n" % total)
for ii in range(0, len(data)):
    Ti = data[ii].get('unit_cell_formula').get('Ti')
    N = data[ii].get('unit_cell_formula').get('N')
    Al = data[ii].get('unit_cell_formula').get('Al')
    Cr = data[ii].get('unit_cell_formula').get('Cr')
    Mn = data[ii].get('unit_cell_formula').get('Mn')
    Ge = data[ii].get('unit_cell_formula').get('Ge')
    if data[ii].get("formation_energy_per_atom") < 0:
        if Ti == None and N != None:
            pass
        elif (Mn == None and Ge != None) or (Mn != None and Ge == None):
            pass
        elif (Ti != None and N != None) and N > Ti:
            pass
        elif (Mn != None and Ge != None) and Mn != 2*Ge:
            pass
        else:
            f.write("%s \n\n" % data[ii])
    else:
        pass

f.close()
