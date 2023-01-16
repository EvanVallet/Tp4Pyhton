date = input("Saisir une date sous la forme jjmmaaaa : ")

jj = date[0:2]
mm = date[2:4]
aaaa = date[:5]

j, m, a = int(jj), int(mm), int(aaaa)
nb_j = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if a % 4 == 0 and a % 100 == 1 or a % 400 == 0:
    nb_j[1] = 29

while len(date) < 5 or j > nb_j[m - 1]:
    print("format de date non valide")
    date = input("Saisir une date sous la forme jjmmaaaa : ")
else:
    print("format de date valide")
