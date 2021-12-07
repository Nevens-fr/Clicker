import Affichable
import Draw

class Bouton(Affichable.affichable):

    #Constructeur
    def __init__(self, coords, path):
        super().__init__(coords, path)

    #Affichage
    def afficher(self, screen):
        Draw.drawBlit(screen, self)