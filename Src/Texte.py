import Draw
import commun
import Affichable

#Permet de contenir du texte
class Texte(Affichable.affichable):

    #Constructeur
    def __init__(self, coords, txt, font, color):
        self.font = font
        self.img = Draw.rendertexte(font, txt, True, color)
        self.coords = coords
        self.color = color

    #Setter du texte
    def setImg(self, txt):
        self.img = Draw.rendertexte(self.font, txt, True, self.color)