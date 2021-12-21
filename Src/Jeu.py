import Draw
import commun
import Affichable
import Bouton
import Click
import Fonctions
import Points
import sys

#Ecran de jeu
def jeu(screen):
    font = Draw.creerFont()
    commun.POINTS = Points.Points(font)
    
    btns = Fonctions.createButtonUpgrade()
    btns.append(Bouton.Bouton(commun.COOKIE_COORD, commun.BTNPATH + commun.COOKIE, Fonctions.addPt))

    arrierePlan = Affichable.affichable(commun.FOND_COORDS, commun.PATH+ commun.FOND)
    click = Click.Click()

    while True:
        click.update()
        Draw.clearScreen(screen)
        arrierePlan.afficher(screen)
        commun.POINTS.afficher(screen)

        for elem in btns:
            try:
                elem.afficher(screen, font)
            except:#exception pour gérer l'affichage du bouton cookie
                elem.afficher(screen)

            if(click.isClicked() and elem.isHover(Draw.mousePos())):
                elem.appliqueMethode()
                click.removeClick()

        Draw.drawScreenUpdate()
        if Draw.quitter():
            commun.POINTS.saveScore(btns)
            sys.exit()