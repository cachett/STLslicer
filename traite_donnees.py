#!/usr/bin/env python3

"""
traite les donnees pour un z donné
"""
class Point:
    """
    A importer
    """
    def __init__(self, abscisse, ordonnee, cote=None):
        self.abs = abscisse
        self.ord = ordonnee
        self.cot = cote

    def __str__(self): #Utile seulement pour les tests
        return "({},{},{})".format(str(self.abs), str(self.ord), str(self.cot))



def filtre_donnees(donnee, h):
    """
    Selectionne les segments coupés
    """
    donnees_filtrees = []
    for i in range(2, len(donnee), 9): #traite triangle par triangle, teste les 3 segments
        if (donnee[i]-h)*(donnee[i+3]-h) < 0:  #si les z sont de part et d'autre de h
            donnees_filtrees += [(Point(donnee[i-2], donnee[i-1], donnee[i]), Point(donnee[i+1], donnee[i+2], donnee[i+3]))]
        if (donnee[i]-h)*(donnee[i+6]-h) < 0:
            donnees_filtrees += [(Point(donnee[i-2], donnee[i-1], donnee[i]), Point(donnee[i+4], donnee[i+5], donnee[i+6]))]
        if (donnee[i+3]-h)*(donnee[i+6]-h) < 0:
            donnees_filtrees += [(Point(donnee[i+1], donnee[i+2], donnee[i+3]), Point(donnee[i+4], donnee[i+5], donnee[i+6]))]
    return donnees_filtrees




def intersection(segment, h):
    """
    retourne les coordonnées des points d'intersection des segments selectionnés et du plan z=h
    """
    data_finale = []
    for elt in segment:#tuple
        coord_x = (elt[1].abs-elt[0].abs)*(h-elt[0].cot)/(elt[1].cot-elt[0].cot)+elt[0].abs
        coord_y = (elt[1].ord-elt[0].ord)*(h-elt[0].cot)/(elt[1].cot-elt[0].cot)+elt[0].ord
        data_finale.append(Point(coord_x, coord_y))
    return data_finale


def find_bornes(donnee):
    """
    trouve et retourne les bornes de chaque coordonnée
    """
    xmin = min(donnee[i] for i in range(0, len(donnee), 3))
    xmax = max(donnee[i] for i in range(0, len(donnee), 3))
    ymin = min(donnee[i] for i in range(1, len(donnee), 3))
    ymax = max(donnee[i] for i in range(1, len(donnee), 3))
    zmin = min(donnee[i] for i in range(2, len(donnee), 3))
    zmax = max(donnee[i] for i in range(2, len(donnee), 3))
    return xmin, xmax, ymin, ymax, zmin, zmax
