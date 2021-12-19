import Draw
import Affichable
import commun
import Jeu
import threading
import Fonctions

#thread pour la création des grandeurs supérieures
thread1 = threading.Thread(target=Fonctions.incrementeGrandeur)
thread1.start()

screen = Draw.create_window(commun.WIDTH, commun.HEIGHT, commun.NAME, Draw.createImg(commun.PATH + commun.ICONE))
t = Affichable.affichable((commun.WIDTH *0.15,commun.HEIGHT* 0.1), commun.PATH + commun.LOGO)
Draw.drawBlit(screen, t)
Draw.drawScreenUpdate()
#Draw.attente(1500)
Jeu.jeu(screen)

#pyinstaller --add-data "../Assets/;./Assets/" main.py
#commande de compilation