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
    def ajout(self, nb, ind):
        try:
            if self.ordre[ind].add(nb):
                self.ordre.append(self.ordre[-1].retourneNextGrandeur())
        except:
            self.ordre.append(self.ordre[-1].createGrandeurLoad(0))
            self.ajout(nb, ind)

    #Affichage
    def afficher(self, screen):
        string = str(self.ordre[-1].getNB()) + " " + self.ordre[-1].getIntitule()
        if len(self.ordre) > 1:
            string += " " +str(self.ordre[-2].getNB()) + " " + self.ordre[-2].getIntitule()
        self.img = Draw.rendertexte(self.font, string, True, self.color)
        Draw.drawBlit(screen, self)

        #retourne l'indice du premier espace d'une chaine
    def getFirstSpace(m):
        i = 0
        for e in m:
            if e == ' ':
                return i
            i += 1

    #Lit le score sur les fichier
    def loadScore(self):
        tmp = 0
        try:
            f = open(commun.PATH + commun.SAVE, "r")
            tmp = f.readlines()
            f.close()
            print(tmp)
            #Valeur de cookie par click plus ordre de grandeur
            commun.COOKIE_CLICK_NB = int(tmp[0][0:self.getFirstSpace(tmp[0])])
            commun.COOKIE_CLICK_NB_ORD_GRAND = int(tmp[0][self.getFirstSpace(tmp[0]) + 1 : ])

            commun.UPGRADE.clear()
            #get des valeurs + ordre de grandeurs des upgrades
            for i in range(1,5):
                commun.UPGRADE.append([int(tmp[i][0:self.getFirstSpace(tmp[0])]), int(tmp[i][self.getFirstSpace(tmp[0]) + 1 : ])])

            #< à 1 000 get des centaines
            self.ordre.append(OrdreGrandeur.OrdreGrandeur("", int(tmp[5]), 0))
            #> à 1 000
            i = 6
            while i < len(tmp) - 1:
                self.ordre.append(self.ordre[-1].createGrandeurLoad(int(tmp[i])))
                i+=1
        except:
            commun.NB = tmp
            commun.UPGRADE= [
                [0,1],
                [0,2],
                [1,3],
                [2,1]
            ]   
            self.ordre.append(OrdreGrandeur.OrdreGrandeur("", tmp, 0))

    #sauvegarde du score
    def saveScore(self, btns):
        try:
            f = open(commun.PATH + commun.SAVE, "w")
            #ecriture des valeurs de cookies par click plus ordre de grandeur
            f.write(str(commun.COOKIE_CLICK_NB) + " " + str(commun.COOKIE_CLICK_NB_ORD_GRAND) + "\n")
            #ecriture des upgrades
            i = 0
            while i < len(btns) - 1:
                f.write(str(btns[i].getIndice()) + " " +str(btns[i].getVal()) +"\n")
                i+=1
            #ecriture des grandeurs
            for e in self.ordre:
                f.write(str(e.getNB())+"\n")
            f.close()
        except:
            print("Error, ecriture dans sauvegarde impossible")