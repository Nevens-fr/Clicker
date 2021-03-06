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

    ##
    #Ajoute nb cookies par click à un ordre de grandeur à l'indice indice
    def ajoutCookieParClick(self, nb, indice):
        self.ordre[indice].ajoutNbParClick(nb)

    ##
    #Retire des cookies par click
    def retirerCookiesParClick(self, indice, val):
        if indice == len(self.ordre):
            self.ordre.append(self.ordre[-1].createGrandeurLoad(0,0))
        elif indice > len(self.ordre):
            while indice >= len(self.ordre):
                self.ordre.append(self.ordre[-1].createGrandeurLoad(0,0))
        self.ordre[indice].retraitParClick(val)

    ##
    #Ajoute des cookies au total
    def ajout(self):
        try:
            i = 0
            while i < len(self.ordre):
                if self.ordre[i].add():
                    self.ordre.append(self.ordre[-1].retourneNextGrandeur())
                i+=1
        except:
            self.ordre.append(self.ordre[-1].createGrandeurLoad(0, 1))
            self.ajout()

    ##
    #Affichage du nombre de cookies possédés
    def afficher(self, screen):

        indPrems = -1

        #Permet de récupérer la première classe pas à 0
        if len(self.ordre) > 1:
            while self.ordre[indPrems].getNB() == 0:
                indPrems -= 1
                if indPrems * (-1) > len(self.ordre):
                    indPrems = 0
                    break
        string = str(self.ordre[indPrems].getNB()) + " " + self.ordre[indPrems].getIntitule()

        indNext = indPrems - 1

        try:
            if len(self.ordre) > 1 and indPrems != 0:
                string += " " +str(self.ordre[indNext].getNB()) + " " + self.ordre[indNext].getIntitule()
        except:
            indNext = None

        textCookieParClick = Texte.Texte(commun.NB_COOKIES_CLICK_COORDS, self.nbCookiesParClick(), self.font, self.color)
        
        self.img = Draw.rendertexte(self.font, string, True, self.color)
        Draw.drawBlit(screen, textCookieParClick)
        Draw.drawBlit(screen, self)

    ##
    #Retourne une chaine de caractère contenant le nombre de cookies par clicks
    def nbCookiesParClick(self):
        string =  string = str(self.ordre[-1].getNBPARCLICK()) + " " + self.ordre[-1].getIntitule()

        if len(self.ordre) > 1:
            string += " "  +str(self.ordre[-2].getNBPARCLICK()) + " " + self.ordre[-2].getIntitule()

        return string

    ##
    #retourne l'indice du premier espace d'une chaine
    def getSpace(self, nb, m):
        i = 0
        for e in m:
            if e == ' ' and nb == 0:
                return i
            elif e == ' ':
                nb-=1
            i += 1
    
    ##
    # AJout un ordre de grandeur
    def addGrandeur(self, grandeur):
        self.ordre.append(grandeur)

    ##
    #Lit le score sur les fichier
    def loadScore(self):
        tmp = 0
        try:
            f = open(commun.PATH + commun.SAVE, "r")
            tmp = f.readlines()
            f.close()

            #arrangement des données
            tmp = ''.join(tmp)
            tmp = tmp.split('\n')
            tmp.pop()            

            commun.UPGRADE.clear()
            #get des valeurs + ordre de grandeurs des upgrades
            for i in range(4):
                commun.UPGRADE.append([int(tmp[i][0:self.getSpace(0,tmp[i])]), int(tmp[i][self.getSpace(0,tmp[i]) + 1 : ])])

            #< à 1 000 get des centaines
            self.ordre.append(OrdreGrandeur.OrdreGrandeur("", int(tmp[4][0:self.getSpace(0,tmp[4])]), 0, int(tmp[4][self.getSpace(0,tmp[4]) + 1 : ])))
            #> à 1 000
            i = 5
            while i < len(tmp):
                self.ordre.append(self.ordre[-1].createGrandeurLoad(int(tmp[i][0 : self.getSpace(0,tmp[i])]), int(tmp[i][self.getSpace(0,tmp[i]) + 1 : ]) ))
                i+=1
        except: #Problème de sauvegarde inexistante ou corrompue, reset de la partie
            commun.UPGRADE= [
                [0,1],
                [0,2],
                [1,3],
                [2,1]
            ]   
            self.ordre.append(OrdreGrandeur.OrdreGrandeur("", tmp, 0, 1))

    ##
    #sauvegarde de la partie
    def saveScore(self, btns):
        try:
            f = open(commun.PATH + commun.SAVE, "w")

            #ecriture des upgrades
            i = 0
            while i < len(btns) - 1:
                f.write(str(btns[i].getIndice()) + " " +str(btns[i].getVal()) + "\n")
                i+=1
            #ecriture des grandeurs
            for e in self.ordre:
                f.write(str(e.getNB())+" "+str(e.getNBPARCLICK())+"\n")
            f.close()
        except:
            print("Error, ecriture dans sauvegarde impossible")