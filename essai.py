""" Cette fonction sert à créer une liste à partir de la combinaison choisie par le joueur
---------------------------------------------------------------------------------------
    ARGUMENTS :
        list ["lettre", i] : str, int      lettre qui correspond à 1 des 4 cercles et nombre à sa couleur
        list [a,b,c,d] : int                liste précédente des combinaisons du joueur

---------------------------------------------------------------------------------------
    SORTIE :
        list [a,b,c,d]  : int     liste des combinaisons du joueur màj
---------------------------------------------------------------------------------------
    """


def essai(lst,combijoueur):
    if lst[0] == "a":
        combijoueur = (lst[1], combijoueur[1], combijoueur[2], combijoueur[3])
    elif lst[0] == "b":
        combijoueur = (combijoueur[0], lst[1], combijoueur[2], combijoueur[3])
    elif lst[0] == "c":
        combijoueur = (combijoueur[0], combijoueur[1], lst[1], combijoueur[3])
    elif lst[0] == "d":
        combijoueur = (combijoueur[0], combijoueur[1], combijoueur[2], lst[1])
    return combijoueur