import commun
import Bouton
import Draw
import Texte

#Gestion des boutons d'upgrade
class BoutonUpgrade(Bouton.Bouton):

    def __init__(self, coords, path, meth, indice, val, txt):
        super().__init__(coords, path, meth)
        self.indice = indice
        self.val = val
        self.txt = txt
    ##
    #Getter val
    def getVal(self):
        return self.val

    ##
    #Getter indice
    def getIndice(self):
        return self.indice

    ##
    #Override affichage classe pour rajouter le texte
    def afficher(self, screen, font):
        super().afficher(screen)
        Draw.drawBlit(screen, Texte.Texte(self.coords, self.txt, font, commun.BLACK))

    ##
    #Ajout de cookies par click en plus
    def appliqueMethode(self):
        oldVal = self.val
        self.val = int(self.val * commun.COEF_UPGRADE + self.val)
        if self.val == oldVal :
            self.val +=1
        elif self.val >= 1000:
            self.indice += 1
            self.val = self.val - 999
        commun.POINTS.retirerCookiesParClick(self.indice, self.val)
        commun.POINTS.ajoutCookieParClick(self.val, self.indice)