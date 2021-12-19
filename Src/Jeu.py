import Draw
import commun
import Affichable
import Bouton
import Click
import Texte
import Fonctions
import Points

#Ecran de jeu
def jeu(screen):
    btns = Fonctions.createButtonUpgrade()
    btns.append(Bouton.Bouton(commun.COOKIE_COORD, commun.BTNPATH + commun.COOKIE, Fonctions.addPt))

    arrierePlan = Affichable.affichable(commun.FOND_COORDS, commun.PATH+ commun.FOND)
    font = Draw.creerFont()
    click = Click.Click()

    commun.POINTS = Points.Points(font)

    while True:
        click.update()
        Draw.clearScreen(screen)
        arrierePlan.afficher(screen)
        commun.POINTS.afficher(screen)

        for elem in btns:
            elem.afficher(screen)
            if(click.isClicked() and elem.isHover(Draw.mousePos())):
                elem.appliqueMethode()
                click.removeClick()

        Draw.drawScreenUpdate()
        Draw.quit()