import commun

class OrdreGrandeur:

    def __init__(self, intitule, nb, indice):
        self.nb = nb
        self.intitule = intitule
        self.indice = indice
        self.suiv = None

    #getter indice
    def getIndice(self):
        return self.indice

    #getter intitulé
    def getIntitule(self):
        return self.intitule

    #getter nb
    def getNB(self):
        return self.nb

    #retourne l'ordre de grandeur suivant
    def retourneNextGrandeur(self):
        nb = self.nb - 999
        self.nb = (1000 - self.nb) * (0-1)
        self.suiv =  OrdreGrandeur(commun.GRANDEURS[self.indice + 1], nb, self.indice + 1)
        return self.suiv

    #créer et retourne le prochain ordre de grandeur pendant le chargement
    def createGrandeurLoad(self, nb):
        self.suiv =  OrdreGrandeur(commun.GRANDEURS[self.indice + 1], nb, self.indice + 1)
        return self.suiv

    #ajoute un nombre à l'instance.
    #Si la classe est en débordement, on renvoit true pour la création d'une instance
    #sinon si besoin on transvase le surplus à l'ordre suivant (retour True si débordement d'un ordre suivant)
    #Renvoie False si aucun débordement
    def add(self, nb):
        self.nb += nb
        if self.debordement():
            return True
        elif self.nb >= 1000:
            nb1 = self.nb - 999
            self.nb = (1000 - self.nb) * (0-1)
            if self.suiv.add(nb1):
                return True
        return False

    #retourne vrai si le nombre est >  à 100 et pas de suivant
    def debordement(self):
        if self.nb >= 1000 and self.suiv == None:
            return True
        else:
            return False
