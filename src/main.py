from carte import *

carte_joueur1 = Carte("as", "coeur")
carte_joueur2 = Carte("as", "trefle")

print("carte du joueur 1: ", carte_joueur1)
print("carte du joueur 2: ", carte_joueur2)

carte_joueur1.dessin(100, 100)
carte_joueur2.dessin(120, 120)

Mafenetre.mainloop()