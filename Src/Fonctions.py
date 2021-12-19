import commun
import Bouton

##
#Créée et retourne la liste des boutons à afficher sur la page
def createButtonUpgrade():
    btns = []
    for elem in commun.BTN_UPGRADE:
        btns.append(Bouton.Bouton(elem, commun.BTNPATH + commun.BUTTONBAR, None))

    return btns

##
#ajoute des points au compteurs et met à jour l'affichage
def addPt(self):
    commun.POINTS.ajout(commun.COOKIE_CLICK_NB)