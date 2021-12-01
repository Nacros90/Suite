print("Ce programme sert à générer une suite géométrique fini avec une valeur U0 et un raison q défini par l'utilisateur.")
print()
U=int(input("Valeur de \"U0\" : "))
U0=U
q=int(input("Valeur de la raison \"q\" : "))
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
print("Fin de la suite.")