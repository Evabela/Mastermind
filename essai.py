def essai(chiffres) :
    """ Cette fonction sert à créer une liste à partir des nombres donnés par le joueur
        
    ARGUMENTS :
    chiffres : str             saisie des 4 nombres du joueur sans espaces
    SORTIE
        liste [a,b,c,d]  : int     retourne les couleurs du joueur sous forme de liste + boléen
    """
   
    combijoueur = []

    for chiffre_str in chiffres : 
        chiffre_int = int(chiffre_str)

        if 1 <= chiffre_int <= 8:
            combijoueur.append(chiffre_int)
        else:
            print("Erreur :", chiffre_int, "n'est pas dans la plage autorisée (1 à 8).")
            return False
        

    return True, combijoueur 

 

if __name__ == "__main__":
    print("****** test *****")
    combi=essai("1238")
    print(combi)