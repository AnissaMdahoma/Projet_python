""" Permet de séparer les différentes chaînes d'un fihchier PDB 
	En prenant en entrée un fichier PDB, il lit le fichier PDB, séparer les  chaînes en deux fichiers 
	et écrit de nouveau fichier PDB avec une unique chaine"""

from python import read_pdb,write_pdb,select_atoms
import argparse
import numpy as np


def parser_input():
	parser = argparse.ArgumentParser(
		description='Prend en entrée un fichier PDB, et le sépare en plusieurs pour chaque chaine.')
	parser.add_argument("-f",action="store",dest="f",type= str,help = "donnez le fichier pdb",required = True)


	return (parser)

def split_chains(df):
	chaines = np.unique(df["chain_identifier"])
	for chain in chaines :
		selection = select_atoms(df,selector={"chain_identifier":[chain]})
		write_pdb(selection,'chaine'+chain+'.pdb')


def main():
    """Main fonction"""
    df = read_pdb(args.f)
    split_chains(df)


if __name__ == '__main__':
	parser=parser_input()
	args = parser.parse_args()
	print('Input file = {}'.format(args.f))
	main()




