import commun
import Bouton
import BoutonUpgrade

##
#Créée et retourne la liste des boutons à afficher sur la page
def createButtonUpgrade():
    btns = []
    ind = 0
    for elem in commun.BTN_UPGRADE:
        tmp = BoutonUpgrade.BoutonUpgrade(elem, commun.BTNPATH + commun.BUTTONBAR, None, commun.UPGRADE[ind][0], commun.UPGRADE[ind][1], commun.TXT_UPGRADE[ind])
        btns.append(tmp)
        ind += 1

    return btns

##
#ajoute des cookies au compteurs car click sur le cookie recu et met à jour l'affichage
def addPt(self):
    commun.POINTS.ajout()



#Créer une string de length éléments l
def createA(l, length):
    return ''.join(([l]*length))

#Retourne vrai si une liste est composée du même élément
def sameL(m):
    m1 = m[0]
    for elem in m:
        if m1 != elem:
            return False
    return True

#Renvoie la position du premier Z dans une liste
def findFirstZ(m):
    ind = 0
    for e in m:
        try:
            if e == 'z' and m[ind + 1] == 'z':
                return ind
        except:
            return ind
        ind += 1

#Incrémente la taille de la liste des grandeurs possibles jusqu'a 3 lettres
def incrementeGrandeur():
    while len(commun.GRANDEURS[-1]) < 4:
        if len(commun.GRANDEURS[-1]) == 1 and commun.GRANDEURS[-1] == "z":
            commun.GRANDEURS.append("aa")
        elif len(commun.GRANDEURS[-1]) == 1:
            commun.GRANDEURS.append(chr(ord(commun.GRANDEURS[-1]) + 1))
        else:
            if sameL(commun.GRANDEURS[-1]) and commun.GRANDEURS[-1][0] == "z": 
                commun.GRANDEURS.append(createA('a', len(commun.GRANDEURS[-1]) +1 ))
            elif sameL(commun.GRANDEURS[-1]) == False and commun.GRANDEURS[-1][-1] == "z":
                b = commun.GRANDEURS[-1]
                b = b[0:findFirstZ(b) - 1] + chr(ord(b[findFirstZ(b)-1]) + 1) + ''.join(['a']* (len(b) - findFirstZ(b)))
                commun.GRANDEURS.append(b)
            else:
                b = commun.GRANDEURS[-1]
                b = b[0:-1] + chr(ord(b[-1])+1)
                commun.GRANDEURS.append(b)