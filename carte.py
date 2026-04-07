# Créé par F, le 02/04/2019 en Python 3.4
from tkinter import *
import random

Mafenetre = Tk()

LARGEUR = 500 # en pixels
HAUTEUR = 400

MonCanevas = Canvas(Mafenetre, width = LARGEUR, height = HAUTEUR, bg = 'black')
MonCanevas.pack(side = TOP, padx = 10, pady = 10)


class Carte:
    """Représente une carte à jouer standard."""
    liste_couleurs = ['trefle', 'carreau', 'coeur', 'pique']
    liste_valeurs = ['2', '3', '4', '5', '6', '7',
                            '8', '9', '10', 'valet', 'dame', 'roi', 'as']

    def __init__(self, valeur = '8', couleur = 'trefle' ):
        self.couleur = couleur
        self.valeur = valeur
        self.image_carte = PhotoImage(file = 'cards_gif/' + valeur + '_' + couleur + '.gif')

    def __str__(self):
        return '%s de %s' % (self.valeur,
                             self.couleur)

    def __lt__(self, autre):
        t1 = Carte.liste_valeurs.index(self.valeur)+2
        t2 = Carte.liste_valeurs.index(autre.valeur)+2
        return t1 < t2

    def __gt__(self, autre):
        t1 = Carte.liste_valeurs.index(self.valeur)+2
        t2 = Carte.liste_valeurs.index(autre.valeur)+2
        return t1 > t2

    def __ge__(self, autre):
        t1 = Carte.liste_valeurs.index(self.valeur)+2
        t2 = Carte.liste_valeurs.index(autre.valeur)+2
        return t1 >= t2

    def __le__(self, autre):
        t1 = Carte.liste_valeurs.index(self.valeur)+2
        t2 = Carte.liste_valeurs.index(autre.valeur)+2
        return t1 <= t2

    def __eq__(self, autre):
        t1 = Carte.liste_valeurs.index(self.valeur)+2
        t2 = Carte.liste_valeurs.index(autre.valeur)+2
        return t1 == t2

    def __ne__(self, autre):
        t1 = Carte.liste_valeurs.index(self.valeur)+2
        t2 = Carte.liste_valeurs.index(autre.valeur)+2
        return t1 != t2

    def dessin(self, x, y):
        return MonCanevas.create_image(x, y, image=self.image_carte, state='normal')


carte_retournee=Carte('0', 'retournee')