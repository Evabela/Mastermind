import pygame
from essai import *
from init import *
from clic import *

print("Il faut cliquer sur les ronds au centre de l'image pour changer leur couleur. Lorsque vous êtes sûr de votre \
      combinaison, appuyez sur entrée. Si rien ne se passe, appuyez sur la touche entrée à une intervalle de 2sec\
      jusqu'à ce que des ronds blancs, noirs ou gris foncé apparaissent. Rond noir = Bonne place ; Blanc = Mauvaise \
      place et gris = n'existe pas")

surf = pygame.display.set_mode((1200,400))
surf.fill((198,198,198)) #fond d'écran
run = True
posX = 200
posb =50
posc = 200
pox =1000 # x de cercles de rappels
poy = 35 # y de cercles de rappels et minis n et b
nb=1
x=40
px= 950 # x de mini n et b
xx=15
cmb = (1,1,1,1)
coups=10
clock=pygame.time.Clock() #vitesse du jeu (plus petit au plus grand)

for i in range (1,5): #définit les 4 premiers cercles
    pygame.draw.circle(surf, (0,0,0), (posX*i, 200), 80, 80)

for i in range (1,11): #cercles à côtés qui rappellent ce qu'on a fait
    for j in range (1,5):
        pygame.draw.circle(surf, (0,0,0), (pox+(j*x), poy*i), 15, 15)


def couleur(nbr): #retourne une couleur selon le chiffre qui rentre
    clr = { 1: (0,0,0), 2: (255, 110, 101), 3: (255, 190, 101), 4: (255, 241, 101),
           5: (178, 255, 101), 6: (101, 255, 190), 7: (101, 115, 255), 8: (201, 101, 255)}

    cl = clr[nbr]

    return cl

def circle(nbr,XY):
    pygame.draw.circle(surf, (nbr), (XY[0],XY[1]), 80, 80)

def rappel(cleurs,result,nbcoups): #programme qui nous rappelle sur le côté nos anciennes combinaisons

#cleurs = list ; result = list str ; nbcoups = int
    clr = { 1: (0,0,0), 2: (255, 110, 101), 3: (255, 190, 101), 4: (255, 241, 101),
           5: (178, 255, 101), 6: (101, 255, 190), 7: (101, 115, 255), 8: (201, 101, 255)}

    cody={0:35,1:70,2:105,3:140,4:175,5:210,6:245,7:280,8:315,9:350} #hauteur en fonction du nombre de coups qu'il reste
    
    for i in range (0,4):
        cord={0:(1040,cody[nbcoups]), 1:(1080,cody[nbcoups]), 2:(1120,cody[nbcoups]),3:(1160,cody[nbcoups])}
        pygame.draw.circle(surf, (clr[cleurs[i]]), (cord[i]), 15, 15)

    for j in range (0,4): #couleurs N, B ou gris
        coord={0:(965,cody[nbcoups]), 1:(980,cody[nbcoups]), 2:(995,cody[nbcoups]),3:(1010,cody[nbcoups])}
        if result[j]=="N":
            pygame.draw.circle(surf, (0,0,0), (coord[j]), 5, 5)
        elif result[j]=="B":
            pygame.draw.circle(surf, (255,255,255), (coord[j]), 5, 5)
        elif result[j]==None :
            pygame.draw.circle(surf, (98,98,98), (coord[j]), 5, 5)

def test(initial,reponse): #B si le pion est mal placé et N si bien placé sinon None
    resultat = [None for i in range(4)]
    for i in range(0,4):
        for j in range(0,4):
            if reponse[i] == initial[i]:
                resultat[i] = "N"
            elif reponse[i] == initial[j]:
                resultat[i] = "B"
    return resultat

def verifc(result): #mise en forme de la fonction test
    for j in range (4):
        coord={0:(200,330), 1:(400,330), 2:(600,330),3:(800,330)}  
        if result[j]=="N":
            pygame.draw.circle(surf, (0,0,0), (coord[j]), 20, 20)
        elif result[j]=="B":
            pygame.draw.circle(surf, (255,255,255), (coord[j]), 20, 20)
        elif result[j]==None :
            pygame.draw.circle(surf, (98,98,98), (coord[j]), 20, 20)
        
for i in range (1,5): #initialisation cercles de vérifications N et B sur gris
    pygame.draw.circle(surf, (198,198,198), (posc*i, 330), 20, 20)

for i in range (1,9): #les couleurs possibles sont montrées à l'utilisateur
        pygame.draw.circle(surf, (couleur(i)), (posb*i, 50), 20, 20)

initiale = init() #la combinaison est choisie par l'ordinateur

while coups != 0 :
    for event in pygame.event.get(): #pygame.event.get crée un tableau avec tous les évènements qui pourrait survenir
        if event.type == pygame.QUIT: #si il y a un évènement qui ferme la fenêtre, alors ça ferme le jeu
            coups = 0

    clock.tick(5) #vitesse du jeu 
    

    if pygame.mouse.get_pressed() == (1,0,0) : #clic gauche détecté
        pos = pygame.mouse.get_pos() #on ajoute les coordonnées du clic à pos
        xy=clic(pos) #on détecte son intervalle pour tracer le cercle à une coordonnée fixe avec la fonction
        nb+=1
        if nb >8 :
            nb=1
        clrs = couleur(nb) #clrs = couleur selon le nombre qui change à chaque clic
        ret = circle(clrs,xy)
        liste= (xy[2],nb) #xy[2]= lettre qui correspond à un cercle, et nb = couleur du cercle
        cmb = essai(liste,cmb) #prend la liste cmd et l'actualise
    
    if event.type == pygame.KEYDOWN : #si la touche entrée est pressée, alors il y a une vérification des combinaisons
      if event.key == pygame.K_RETURN :
        verification = test(initiale,cmb)
        verifc(verification) #mise en forme de vérification
        coups-=1
        rappel(cmb,verification,coups)
        

        if verification == ["N","N","N","N"]:
            print(f"Vous avez gagné en {10-coups} coups ! Victoire!!!")
            coups = 0


    pygame.display.flip()

if verification != ["N","N","N","N"] and coups == 0:
    print(f"vous avez perdu la combinaison était {initiale}")

pygame.quit() #on quitte le jeu