nMax = 3
n = int(input("Quelle est la taille de vos vecteur [entre 1 et 3] : "))

v1 = []
v2 = []
scal = 0.0
while not n <= nMax :
    print("La taille de vos vecteur est trop grande !")
    n = float(input("Quelle est la taille de vos vecteur [entre 1 et 3] : "))

print("Saisie du premier vecteur")
for i in range(n):
    v1.append(float(input("v1[{}] : ".format(i))))

print("Saisie du deuxième vecteur")
for i in range(n):
    v2.append(float(input("v2[{}] : ".format(i))))

for i in range(n):
    scal += v1[i] * v2[i]

print("Le produit scalaire de v1 par v2 vaut {}".format(scal))