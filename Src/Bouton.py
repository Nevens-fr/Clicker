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

        #recupère les dimensions de l'image
        self.w = Draw.imgSize(self.img)[0]
        self.h = Draw.imgSize(self.img)[1]

        self.cptUpdate = 0
        self.maxCpt = 150

    #Renvoie vrai si la position passée en paramètre est dans l'image
    def isHover(self, position):
        w = position[0]
        h = position[1]
        ret = False

        if w >= self.coords[0] and w <= self.w + self.coords[0]:
            if h >= self.coords[1] and h <= self.h+self.coords[1]:
                ret = True
                self.setImgC()
        return ret

    #Change l'image affichée car souris au dessus img
    def setImgH(self):
        self.img = self.imgH

    #Change l'image affichée car bouton cliqué
    def setImgC(self):
        self.img = self.imgC

    #Change l'image affichée car aucune action sur le bouton
    def setImgN(self):
        self.img = self.imgN

    #Override de l'affichage
    def afficher(self, screen):
        super().afficher(screen)

        self.cptUpdate += 1

        if self.cptUpdate == self.maxCpt:
            self.setImgN()
            self.cptUpdate = 0