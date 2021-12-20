import commun

class OrdreGrandeur:

    #self.nb est le nombre de cookies contenus dans cet ordre de grandeur
    #self.intitule est le nom de l'ordre de grandeur (milliers, millions...)
    #self.indice est l'indice dans la list de grandeur (pour accèder au suivant ou précédent)
    #self.suiv est l'élément suivant dans la liste
    def __init__(self, intitule, nb, indice, nb_par_click):
        self.nb = nb
        self.intitule = intitule
        self.indice = indice
        self.suiv = None
        self.nb_par_click = nb_par_click

    ##
    # Ajout un nombre de cookies ajoutés par click à la classepar click
    def ajoutNbParClick(self, nb):
        self.nb_par_click += nb
        if self.nb >= 1000:
            nb1 = self.nb_par_click - 999
            self.nb_par_click = (1000 - self.nb_par_click) * (0-1)
            if self.suiv != None:
                self.suiv.ajoutNbParClick(nb1)
            else:
                self.suiv =  OrdreGrandeur(commun.GRANDEURS[self.indice + 1], 0, self.indice + 1, nb1)
                commun.POINTS.addGrandeur(self.suiv)

    ##
    #Retire des cookies distribués par click
    def retraitParClick(self, nb):
        self.nb_par_click -= nb
        if self.nb_par_click < 0:
            self.nb_par_click = 0


    ##
    #getter indice
    def getIndice(self):
        return self.indice

    ##
    #getter intitulé
    def getIntitule(self):
        return self.intitule

    ##
    #getter nb
    def getNB(self):
        return self.nb

    ##
    #getter nb_par_click
    def getNBPARCLICK(self):
        return self.nb_par_click

    ##
    #retourne l'ordre de grandeur suivant
    def retourneNextGrandeur(self):
        nb = self.nb - 999
        self.nb = (1000 - self.nb) * (0-1)
        self.suiv =  OrdreGrandeur(commun.GRANDEURS[self.indice + 1], nb, self.indice + 1)
        return self.suiv

    ##
    #créer et retourne le prochain ordre de grandeur pendant le chargement
    def createGrandeurLoad(self, nb, nbCPC):
        self.suiv =  OrdreGrandeur(commun.GRANDEURS[self.indice + 1], nb, self.indice + 1, nbCPC)
        return self.suiv

    ##
    #ajoute un nombre de cookies à l'ordre de grandeur
    #Si la classe est en débordement, on renvoit true pour la création d'une instance
    #sinon si besoin on transvase le surplus à l'ordre suivant (retour True si débordement d'un ordre suivant)
    #Renvoie False si aucun débordement
    def add(self):
        self.nb += self.nb_par_click
        if self.debordement():
            return True
        elif self.nb >= 1000:
            nb1 = self.nb - 999
            self.nb = (1000 - self.nb) * (0-1)
            if self.suiv.add(nb1):
                return True
        return False

    ##
    #retourne vrai si le nombre est >  à 100 et pas de suivant
    def debordement(self):
        if self.nb >= 1000 and self.suiv == None:
            return True
        else:
            return False
