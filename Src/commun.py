###
# path d'accès aux ressources
PATH = "./Assets/"
BTNPATH = PATH +"Boutons/"

###
#Caractéristiques fenetre
WIDTH = 850
HEIGHT = 502
NAME = 'CLICKER'

###
#Ressources
LOGO = "logo_NS.png"
ICONE = "cookie.png"
FOND = "fond.png"

SAVE = "save.txt"

POINTS = None

UPGRADE = [
    [0,1],
    [0,2],
    [1,3],
    [2,1]
]

TXT_UPGRADE = [
    "Faits par la grand-maman",
    "Extorsion aux maternelles",
    "Usine locale",
    "Poids lourd de l'industrie"
]

COEF_UPGRADE = 0.25


#boutons
EXT = ".png"

COOKIE = "cookie"
BUTTONBAR = "ButtonBar"

##
# COULEURs
WHITE = (255,255,255)
BLACK = (0,0,0)

##
#Emplacement des boutons
COOKIE_COORD = (WIDTH * 0.21, HEIGHT * 0.48)
FOND_COORDS = (0,0)
NB_COOKIES_COORDS = (50,10)
NB_COOKIES_CLICK_COORDS = (93,45)

BTN_UPGRADE = []
BTN_UPGRADE.append((WIDTH * 0.55, HEIGHT * 0.24))
BTN_UPGRADE.append((WIDTH * 0.55, HEIGHT * 0.43))
BTN_UPGRADE.append((WIDTH * 0.55, HEIGHT * 0.63))
BTN_UPGRADE.append((WIDTH * 0.55, HEIGHT * 0.83))

##
#Grandeurs
GRANDEURS = ["", "milliers", "millions", "milliards", "trilliards", "a"]