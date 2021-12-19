import commun
import Texte
import OrdreGrandeur
import Draw

class Points(Texte.Texte):
    #Constructeur
    def __init__(self, font):
        super().__init__(commun.NB_COOKIES_COORDS, "0", font, commun.BLACK)
        self.ordre = []
        self.loadScore()

    #Ajoute un nombre au total
    def ajout(self, nb):
        if self.ordre[-1].add(nb):
            self.ordre.append(self.ordre[-1].retourneNextGrandeur())

    #Affichage
    def afficher(self, screen):
        string = str(self.ordre[-1].getNB()) + " " + self.ordre[-1].getIntitule()
        if len(self.ordre) > 1:
            string += " " +str(self.ordre[-2].getNB()) + " " + self.ordre[-2].getIntitule()
        self.img = Draw.rendertexte(self.font, string, True, self.color)
        Draw.drawBlit(screen, self)

    #Lit le score sur les fichier
    def loadScore(self):
        tmp = 0
        try:
            f = open(commun.PATH + commun.SAVE, "r")
            tmp = f.readline()
            commun.NB = int(tmp)
            #< à 1 000
            tmp = f.readline()
            self.ordre.append(OrdreGrandeur.OrdreGrandeur("", int(tmp), 0))
            tmp = f.readline()
            #> à 1 000
            while tmp != "":
                self.ordre.append(self.ordre[-1].createGrandeurLoad(int(tmp)))
                tmp = f.readline()
            f.close()
        except:
            commun.NB = tmp
            self.ordre.append(OrdreGrandeur.OrdreGrandeur("", tmp, 0))

    #sauvegarde du score
    def saveScore(self):
        try:
            f = open(commun.PATH + commun.SAVE, "w")
            f.write(str(commun.NB))
            f.close()
        except:
            print("Error, ecriture dans sauvegarde impossible")