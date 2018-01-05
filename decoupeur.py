#!/usr/bin/env python3
"""
fichier principal
"""
#import subprocess à décommenter pour affichage dans terminal avec terminology
#import shlex à décommenter pour affichage dans terminal avec terminology
import sys
import numpy
import extrait_donnees
import tranche_svg
import traite_donnees


def decoupe(fichier, nombre_slices):
    """
    fonction appelant les autres fonctions de differents fichiers
    """
    donnees_points = extrait_donnees.get_data(fichier)
    xmin, xmax, ymin, ymax, zmin, zmax = traite_donnees.find_bornes(donnees_points)
    plans = numpy.linspace(zmin+2, zmax-2, nombre_slices)

    for indice, hauteur in enumerate(plans):
        segments_coupes = traite_donnees.filtre_donnees(donnees_points, hauteur)
        data_finale = traite_donnees.intersection(segments_coupes, hauteur)
        tranche_svg.trace(data_finale, max(xmax-xmin, ymax-ymin), max(xmax-xmin, ymax-ymin), "tranche"+str(indice)+".svg", xmin, ymin)
        #subprocess.call(shlex.split('./affiche_svg.sh tranche'+str(indice)+'.svg')) à décommenter pour affichage dans terminal avec terminology



def main():
    """
    Gère les arguments en ligne de commande puis appelle decoupe
    """
    nombre_slices = 4
    if len(sys.argv) == 1:
        print("utilisation :", sys.argv[0], "[-h] [-s] SLICES stl_file")
        sys.exit(1)
    elif sys.argv[1] == '-h':
        print("utilisation :", sys.argv[0], "[-h] [-s] SLICES stl_file\n\nSlice a STLfile\n\npositionnal argument:\nstl_file\t name of stlfile to slice\n\noptional arguments:\n-h, --help\t show this help message and exit\n-s SLICES\t how many slices do you want(default is 4)\n\nWrites a numbered output svg files for each slices(bottom to top)")
        sys.exit(0)
    elif sys.argv[1] == '-s':
        nombre_slices = int(sys.argv[2])
    decoupe(sys.argv[3], nombre_slices)


main()
