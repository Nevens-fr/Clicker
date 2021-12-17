import Draw
import commun
import Affichable
import Bouton
import Click
import Texte

#Ecran de jeu
def jeu(screen):

    cookie = Bouton.Bouton((commun.WIDTH / 2, commun.HEIGHT / 2), commun.BTNPATH + "cookie")
    font = Draw.creerFont()
    nb = 0
    click = Click.Click()
    txt = Texte.Texte((0,0), str(nb), font, (255,255,255))

    while True:
        click.update()
        Draw.clearScreen(screen)
        txt.afficher(screen)
        cookie.afficher(screen)
        Draw.drawScreenUpdate()
        Draw.quit()

        if(click.isClicked() and cookie.isHover(Draw.mousePos())):
            cookie.setImgC()
            nb += 1
            print(nb)
            txt.setImg(str(nb))
