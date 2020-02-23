#!/usr/bin/env python

from pymatgen import MPRester
from datetime import date

m = MPRester("2fTJ4oel7nxrzFOd")
data = m.query(criteria=
        {"spacegroup.number":{"$in":[75,76,77,78,79,80,81,82,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,168,169,170,171,172,173,174,177,178,179,180,181,182,183,184,185,186,187,188,189,190,195,196,197,198,207,208,209,210,211,212,213,214,215,216,217,218,219,220]}, "band_gap":0, "magnetic_type":{"$in":["FM","AFM","FiM"]}, "nelements":{"$lt":5}, "elements":{"$nin":["Tc","Pm","Ac","Th","Pa","U","Np","Pu"]}}, 
        properties=["pretty_formula", "material_id", "formation_energy_per_atom", "unit_cell_formula", "spacegroup", "structure", "magnetic_type", "total_magnetization"], chunk_size=10)

today = date.today()
d = today.strftime("%Y%m%d")

f = open("MP_%s.txt" % (d), "w+")
for ii in range(0, len(data)):
    if ii == 0:
        f.write("Materials found: %i\n\n" % len(data))
        f.write("%s \n\n" % data[ii])
    else:
        f.write("%s \n\n" % data[ii])

f.close()
