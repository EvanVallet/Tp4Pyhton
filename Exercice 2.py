nombreEtudiant= int(input("Donnez le nombre d'étudiants : "))
moyenne = 0.0;
notes = []
sommeNotes = 0.0
fin = False
noteT = 0.0

for i in range(nombreEtudiant):
    noteT = float(input("Note etudiant {} : ".format(i+1)))
    while not noteT < 0 and noteT > 20:
        print("Veuillez saisir une valeur entre 0 et 20 !")
        noteT = float(input("Note etudiant {} : ".format(i+1)))
    notes.append(noteT)
    sommeNotes += noteT

moyenne = round(sommeNotes / nombreEtudiant, 2)
print(moyenne)
print("Numéro de l'étudiant | note | ecart a la moyenne")
for i in range(nombreEtudiant):
    ah = notes[i]
    ecart = ah - moyenne
    print("{} | {} | {}".format(i, notes[i], ecart))


