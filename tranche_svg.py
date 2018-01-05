#!/usr/bin/env python3



def trace(liste, largeur, hauteur, nom_tranche, xmin, ymin):#xmin et ymin pour recentrer l'image qui contient des coordonnées négative => tout est positif
    """
    Ecrit le fichier svg
    """
    fichier = open(nom_tranche, "w")
    fichier.write('<svg width="{}" height="{}" viewBox="0 0 {} {}" >\n'.format(largeur+300, hauteur+300, largeur+2, hauteur+2))
    #quelques problèmes avec stroke-width, hauteur/400 relation trouvé a la main
    for indice in range(0, len(liste), 2):
        data = '<line x1="{}" x2="{}" y1="{}" y2="{}" stroke="red" stroke-width="{}"/>\n'.format(liste[indice].abs-xmin, liste[indice+1].abs-xmin, liste[indice].ord-ymin, liste[indice+1].ord-ymin, hauteur/200)
        fichier.write(data)
    fichier.write('</svg>')

"""
TEST


aaa = Points(1, 2)
bbb = Points(54, 34)
lll = [aaa, bbb, ccc, ddd]
ccc = Points(44, 86)
ddd = Points(79, 67)
lo = 100
la = 100
print(traceur(lll, lo, la, 'tranche_test'))
"""
