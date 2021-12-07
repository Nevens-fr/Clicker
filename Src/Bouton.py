import Affichable
import Draw
import commun

class Bouton(Affichable.affichable):

    #Constructeur
    def __init__(self, coords, path):
        super().__init__(coords, path + commun.EXT)
        self.imgN = Draw.createImg(path + commun.EXT)               #bouton sans action
        self.imgC = Draw.createImg(path + "C" + commun.EXT)         #bouton cliqué
        self.imgH = Draw.createImg(path + "H" + commun.EXT)         #bouton hover

    #Affichage
    def afficher(self, screen):
        Draw.drawBlit(screen, self)

    #Change l'image affichée car souris au dessus img
    def setImgH(self):
        self.img = self.imgH

    #Change l'image affichée car bouton cliqué
    def setImgC(self):
        self.img = self.imgC

    #Change l'image affichée car aucune action sur le bouton
    def setImgN(self):
        self.img = self.imgN