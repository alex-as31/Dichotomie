print("\nBienvenue dans l'outil servant à résoudre des équations par dichotomie !")
print("\nL'équation est une équation de type : ax + b")
a = int(input("Rentrez ce qui correspond à 'A' dans votre équation : "))
b = int(input("Rentrez ce qui correspond à 'B' dans votre équation : "))
print(f"Votre équation est donc : {a}x + {b}\n")
t = 0
temps = 0

A1 = -100
A2 = 100
A3 = b

image = a * A1 + b
image2 = a * A2 + b

if b == 0:
    print("La solution de l'équation est 0")
    print(f"Il m'a fallut {temps} boucles pour trouver ce résultat")
else:
    for i in range(30):
        temps += 1
        image = a * A1 + b
        image2 = a * A2 + b

        if abs(image) - abs(image2) < 0:
            # Il faut aller à gauche
            A3 = (A1 + A2) / 2
            A2 = A3
            A3 = (A1 + A2) / 2

        elif abs(image) - abs(image2) > 0:
            # Il faut aller à droite
            A3 = (A1 + A2) / 2
            A1 = A3
            A3 = (A1 + A2) / 2

        else:
            print("haaaaaaaaaaaaaaaaaaa")

        s = [abs(A1),abs(A2)]

        if max(s) - min(s) < 0.001:
            print("Votre solution est entre ces deux nombres : ")
            print(round(A1, 5))
            print(round(A2, 5))
            print(f"Il m'a fallut {temps} boucles pour trouver ce résultat")
            break
        else :
            continue