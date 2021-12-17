import Draw

#Gestion du click de souris
class Click:

    #constructeur
    def __init__(self):
        self.click = 0
        self.attenteClick = 300
        self.time = Draw.getTime()

    #Update le dernier click effectué si assez de temps c'est passé
    def update(self):
        if self.click == 0 and Draw.mouseClicked() and self.time + self.attenteClick < Draw.getTime():
            self.click = 1
            self.time = Draw.getTime()

    #renvoi vrai si un click est en mémoire
    def isClicked(self):
        if self.click == 1:
            self.click = 0
            return True
        else:
            return False
    