import Draw
import commun
import Affichable
import Bouton
import Texte

#Ecran de jeu
def jeu(screen):

    cookie = Bouton.Bouton((commun.WIDTH / 2, commun.HEIGHT / 2), commun.BTNPATH + "cookie")
    font = Draw.creerFont()
    nb = 0
    txt = Texte.Texte((0,0), str(nb), font, (255,255,255))

    while True:
        Draw.clearScreen(screen)
        txt.afficher(screen)
        cookie.afficher(screen)
        Draw.drawScreenUpdate()
        Draw.quit()

        if(cookie.isClicked(Draw.mousePos()) and Draw.mouseClicked()):
            cookie.setImgC()
            nb += 1
            print(nb)
            txt.setImg(str(nb))
