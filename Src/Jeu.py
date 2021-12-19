import Draw
import commun
import Affichable
import Bouton
import Click
import Texte

#Ecran de jeu
def jeu(screen):

    cookie = Bouton.Bouton((commun.WIDTH * 0.21, commun.HEIGHT * 0.48), commun.BTNPATH + commun.COOKIE)
    arrierePlan = Affichable.affichable((0,0), commun.PATH+ commun.FOND)
    font = Draw.creerFont()
    nb = 0
    click = Click.Click()
    txt = Texte.Texte((50,10), str(nb), font, (0,0,0))

    while True:
        click.update()
        Draw.clearScreen(screen)
        arrierePlan.afficher(screen)
        txt.afficher(screen)
        cookie.afficher(screen)
        Draw.drawScreenUpdate()
        Draw.quit()

        if(click.isClicked() and cookie.isHover(Draw.mousePos())):
            nb += 1
            txt.setImg(str(nb))
