def clic(posi): #position du cercle en fonction du clic de l'utilisateur
    cx = int
    cy = int
    alb = str

    if posi[0]>120 and posi[0]<280 and posi[1]>120 and posi[1]<280 :
        cx = 200
        cy = 200
        alb = "a"

    if posi[0]>320 and posi[0]<480 and posi[1]>120 and posi[1]<280 :
        cx = 400
        cy = 200
        alb = "b"

    if posi[0]>520 and posi[0]<680 and posi[1]>120 and posi[1]<280 :
        cx = 600
        cy = 200
        alb = "c"       

    if posi[0]>720 and posi[0]<880 and posi[1]>120 and posi[1]<280 :
        cx = 800
        cy = 200
        alb = "d"

    return cx,cy,alb
