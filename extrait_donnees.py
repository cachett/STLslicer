#!/usr/bin/env python3

import struct
"""
extrait les données du STL
"""

def get_data(nom_stl):
    """
    récupère les données du fichier STL sous forme de coordonnées de points
    """
    donnees_points = []
    
    with open(nom_stl, "rb") as f:
        stl_bytes = f.read()
        
    nbr_triangle = (len(stl_bytes)-84)//50
    fmt='<'
    for k in range(nbr_triangle):
        fmt += 'ffffffffffffh'
        
    donnees_temp = struct.unpack(fmt,stl_bytes[84:]) #Tout d"un coup sinon '<' fait tout bugé
    
    for i in range(nbr_triangle): #on tri les données pour avoir que les points
        donnees_points += donnees_temp[i*13+3:i*13+12]
    return donnees_points



