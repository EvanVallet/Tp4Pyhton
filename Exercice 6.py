l = [5, 2, 4, 8, 1, 3]


for i in range(len(l)):
    for j in range(len(l)):
        if l[i] < l[j]:
            tmp = l[j]
            l[j] = l[i]
            l[i] = tmp

    print(l)
