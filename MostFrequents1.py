L1 = [2, 7, 5, 6, 6, 1, 7, 2, 1, 7, 6]
count = 0
retour = 0

for i in range(len(L1)):
    count = 0
    for j in range(len(L1)):
        if L1[i] == L1[j]:
            count += 1
        if count > retour:
            retour = count
            nb = L1[i]


print("Le nombre le plus fréquent dans la liste est le {} ({} x)".format(nb, retour))

