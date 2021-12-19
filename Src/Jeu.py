import Draw
import commun
import Affichable
import Bouton
import Click
import Texte

#Ecran de jeu
def jeu(screen):
    btns = createButtonUpgrade()
    btns.append(Bouton.Bouton(commun.COOKIE_COORD, commun.BTNPATH + commun.COOKIE, addPt))

    arrierePlan = Affichable.affichable(commun.FOND_COORDS, commun.PATH+ commun.FOND)
    font = Draw.creerFont()
    nb = 0
    click = Click.Click()
    commun.TXT_NB_COOKIES = Texte.Texte(commun.NB_COOKIES_COORDS, str(commun.NB), font, commun.BLACK)

    while True:
        click.update()
        Draw.clearScreen(screen)
        arrierePlan.afficher(screen)

        for elem in btns:
            elem.afficher(screen)
            if(click.isClicked() and elem.isHover(Draw.mousePos())):
                elem.appliqueMethode()
                click.removeClick()

        commun.TXT_NB_COOKIES.afficher(screen)
        Draw.drawScreenUpdate()
        Draw.quit()

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
    commun.NB += commun.COOKIE_CLICK_NB
    commun.TXT_NB_COOKIES.setImg(str(commun.NB))
