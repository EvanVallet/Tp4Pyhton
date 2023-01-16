dico={}
dico ['prenom'] = 'Evan'
dico ['nom'] = 'Vallet'
dico ['promo'] = 'rt2025'
dico ['groupe'] = 'rt13'
dico2={}
dico2 ['prenom'] = 'Thomas'
dico2 ['nom'] = 'Rubio'
dico2 ['promo'] = 'rt2025'
dico2 ['groupe'] = 'rt13'
binome = {}
binome ['etudiant 1'] = dico
binome ['etudiant 2'] = dico2
print("- l'etudiant",binome['etudiant 1']['nom'],binome['etudiant 1']['prenom'],'du groupe',binome['etudiant 1']['groupe'])
print("- l'etudiant",binome['etudiant 2']['nom'],binome['etudiant 2']['prenom'],'du groupe',binome['etudiant 2']['groupe'])
