print("Ce programme sert à générer une suite, soit arithmétique, soit géométrique, avec un nombre de pas définissable, une valeur \"U0\" définissable et une raison \"q\" définissable. Toutes les valeurs définissables sont définies par l'utilisateur et doivent être entières.")
Suite=int(input("Quel type de suite voulez générer (1. arithmétique; 2. géométrique) (Veuillez entrez le chiffre corrrepondant à la réponse) ? "))
if Suite==1:
    print()
    U=float(input("Valeur de \"U0\" : "))
    U0=U
    q=float(input("Valeur de la raison \"q\" : "))
    L=int(input("Nombre de pas : "))
    P=0
    print("U0=",U0)
    for k in range (1,L):
        U=U+q
        P=P+1
        print("U",P,"=",U)
        print("Le pas est égale à",k)
        print()
if Suite==2:
    print()
    U=float(input("Valeur de \"U0\" : "))
    U0=U
    q=float(input("Valeur de la raison \"q\" : "))
    L=int(input("Longueur de la suite : "))
    P=0
    print("U0=",U0)
    for k in range (1,L):
        U=U*q
        P=P+1
        print("U",P,"=",U)
        print("Le pas est égale à",k)
        print()
print()
print()
print("Fin de la suite.")