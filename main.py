# Premier projet en python que j'ai fait il y a un an
# Test avec Github

print("\nBienvenue dans l'outil servant à résoudre des équations par dichotomie !")
print("\nL'équation est une équation de type : ax + b")
a = int(input("Rentrez ce qui correspond à 'A' dans votre équation : "))
b = int(input("Rentrez ce qui correspond à 'B' dans votre équation : "))
print("Votre équation est donc : ", a,"x + ", b)
t = 0
temps = 0

A1 = -100
A2 = 100
A3 = a * 0 + b

image = a * A1 + b
image2 = a * A2 + b

print("")

while temps < 30:
    temps = temps + 1
    image = a * A1 + b
    image2 = a * A2 + b

    if abs(image) - abs(image2) < 0:
        #print("Il faut aller à gauche")
        A3 = (A1 + A2) / 2
        A2 = A3
        A3 = (A1 + A2) / 2

    elif abs(image) - abs(image2) > 0:
        #print("Il faut aller à droite")
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
        print("Il m'a fallut", temps, "boucles pour trouver ce résultat")
        break
    else :
        continue