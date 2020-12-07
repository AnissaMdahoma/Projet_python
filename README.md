
# Projet Python 
Le but de ce projet est de rédiger différentes fonctions qui permettent de lire un fichier pdb, écrire un fichier pdb, sélectionner différentes  chaînes et aussi calculer une distance euclidienne entre deux résidus.  


## Pour commencer

Pour exécuter correctement le programme il faut que les fichiers suivants soient dans le même dossier, il faut également télécharger un fichier pdb de son choix. 

- python.py
- split_chains.py
- 1 fichier pdb

### Différentes fonctions 

Le fichier ``python.py`` contient 4 fonctions : 

``read_pdb`` qui lit un fichier pdb passer en entrée et renvoi une dataframe pandas contenant le pdb 

``write_pdb`` qui prend en entrée une dataframe pandas ainsi que le nom du fichier de sortie et renvoi un fichier pdb 

``select_atoms`` qui prend en entrée un dataframe pandas ainsi que la selection d'atome sous la forme d'un dictionnaire et renvoi la sous selection sous la forme d'une dataframe pandas 

``compute_distance`` qui prend en entrée deux lignes d'une dataframe et renvoie la distance entre les deux atomes. 

Le fichier ``split_chain.py`` contient 2 fonctions : 

``parser_input`` qui permet de passer des arguments en ligne de commande 

``split_chains``qui permet de sélectionner une chaîne d'un fichier pdb 

## Pour exécuter la commande

_exemple_: Executez la commande ``python3 split_chains.py -f fichier.pdb -o fichier_sortie.pdb``

## Auteurs
* **Anissa MDAHOMA ** _alias_ [@AnissaMdahoma ](https://github.com/AnissaMdahoma)

