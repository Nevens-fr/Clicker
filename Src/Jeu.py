import Draw
import commun
import Affichable
import Bouton

#Ecran de jeu
def jeu(screen):

    b = Bouton.Bouton((0,0), commun.PATH + commun.BTN)

    while True:
        Draw.clearScreen(screen)
        b.afficher(screen)
        Draw.drawScreenUpdate()
        Draw.attente(150)
        Draw.quit()

