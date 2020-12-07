import math 
import argparse
import numpy as np
import pandas as pd

def read_pdb(fichier_pdb):
    """Lecture d'un fichier PDB
    Extrait les coordonnées de tous les atomes de la protéine dans un data frame pandas et le renvoie."""
    with open(fichier_pdb,"r") as pdb_file:
        liste_principale=[]
        for line in pdb_file:
            if line.startswith("ATOM") or line.startswith("HETATM"): 
                sous_liste=[]
                sous_liste.append(line[0:6])
                sous_liste.append(int(line[6:11]))
                sous_liste.append(line[12:16].strip())
                sous_liste.append(line[16:17])
                sous_liste.append(line[17:20].strip())
                sous_liste.append(line[21:22])
                sous_liste.append(int(line[22:26]))
                sous_liste.append(line[26:27])
                sous_liste.append(float(line[30:38]))
                sous_liste.append(float(line[38:46]))
                sous_liste.append(float(line[46:54]))
                sous_liste.append(float(line[54:60]))
                sous_liste.append(float(line[60:66]))
                sous_liste.append(line[76:78])
                sous_liste.append(line[78:80])
                liste_principale.append(sous_liste)
                
        df= pd.DataFrame(liste_principale, columns = ['ATOM','atom_number','atom_name','location_indicator','residue_name',\
                                                      'chain_identifier','residue_number','code','X','Y','Z',\
                                                     'occupancy','temperature','symbol','charge'])
    return df



def write_pdb(df,nouveau_pdb):
    """ Ecriture d'un fichier PDB 
    Prend le nom du nouveau fichier .pdb et de la data frame pandas dans le même format que celui défini 
    précédemment et l'enregistre au format pdb."""
    with open(nouveau_pdb,"wt") as inputfile:
        for i in range(len(df)):
            inputfile.write("{:6s}{:5d} {:^4s}{:1s}{:3s} {:1s}{:4d}{:1s}   {:8.3f}{:8.3f}{:8.3f}{:6.2f}{:6.2f}          {:>2s}{:2s}\n".format(df.iloc[i,0],df.iloc[i,1],df.iloc[i,2],\
                                                                                                                        df.iloc[i,3],df.iloc[i,4],df.iloc[i,5],df.iloc[i,6],df.iloc[i,7],\
                                                                                                                        df.iloc[i,8],df.iloc[i,9],df.iloc[i,10],df.iloc[i,11],\
                                                                                                                        df.iloc[i,12],df.iloc[i,13],df.iloc[i,14]))
        inputfile.write("TER")
    return inputfile

def select_atoms(df,selector):
    """ Sélection d'atome 
    Prend en entrée la data frame pandas et un selecteur et renvoi une data frame """
    data = df
    for sele in selector: 
        selection = data.loc[data[sele].isin(selector[sele])]
    return selection
    
#def get_aa_seq(df):


def compute_distance(d1,d2):
    '''Calcul la distance entre deux atomes '''
    a = d1
    b= d2
    somme = 0 
    for row in ['X','Y','Z']:
        somme = somme + (b[row]-a[row])**2
    distance = math.sqrt(somme)
    return distance 

#def find_salt_bridges : 

#def contact_map():
























