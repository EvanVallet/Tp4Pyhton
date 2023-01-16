L1 = [2, 7, 5, 6, 6, 1, 7, 2, 1, 7, 6]
n1 = 0
for i in range(len(L1)):
    n = L1.count(L1[i])
    if n > n1:
        n1 = n
        nb = L1[i]
print("Le nombre le plus frequent dans la liste est le : {} ({} x)".format(nb, n1))
