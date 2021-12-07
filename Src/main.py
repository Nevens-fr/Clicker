import Draw
import Affichable
import commun
import Bouton

screen = Draw.create_window(commun.WIDTH, commun.HEIGHT, commun.NAME, Draw.createImg(commun.PATH + commun.ICONE))
t = Affichable.affichable((commun.WIDTH *0.15,commun.HEIGHT* 0.1), commun.PATH + commun.LOGO, (0,0,0))
Draw.drawBlit(screen, t)
Draw.drawScreenUpdate()
Draw.attente(1500)

#pyinstaller --add-data "../Assets/;./Assets/" main.py
#commande de compilation