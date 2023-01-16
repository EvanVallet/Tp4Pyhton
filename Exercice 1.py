n = float(input("Vous cherchez la table de multiplication de quel nombre ? : "))

for i in range(0, 10):
    nb = i*n
    print("{} * {} = {}".format(n, i, round(nb, 2)))
