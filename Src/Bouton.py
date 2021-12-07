import Affichable
import Draw

class Bouton(Affichable.affichable):

    def __init__(self, coords, path, color):
        super().__init__(coords, path, color)

    def afficher(self, screen):
        Draw.drawBlit(screen, self)