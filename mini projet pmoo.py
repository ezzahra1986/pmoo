#existance
def EtudiantExiste(code):
    with open("etudiants.txt", "r") as f:
        for ligne in f:
            txt=ligne.split("\t")
            if txt[0]==code:
                return 1
        return 0
def EnseignantExiste(code):
    with open("enseignants.txt", "r") as f:
        for ligne in f:
            txt=ligne.split("\t")
            if txt[0]==code:
                return 1
        return 0
def CourExiste(code):
    with open("cours.txt", "r") as f:
        for ligne in f:
            txt=ligne.split("\t")
            if txt[0]==code:
                return 1
        return 0
#modification 
def ModifierEtudiant(code,nom,prenom,math,info,langues, filiere):
    if EtudiantExiste(code)==1:
        lignes=[]
        with open("etudiants.txt", "r") as f:
            for ligne in f:
                txt=ligne.split("\t")
                if txt[0]!=code:
                    lignes.append(ligne)
                else:
                    lignes.append(code+"\t"+prenom+"\t"+nom+"\t"+math+"\t"+info+"\t"+langues+"\t"+filiere+"\n")
        f.close()
        with open("etudiants.txt", "w") as f:
            for l in lignes:
                f.write(l)
        f.close()
        print("Etudiant modifié avec succés")
    else: 
        print("Etudiant "+code+" n'existe pas\n")
def ModifierEnseignat(code,nom,prenom,matiere):
    if EnseignantExiste(code)==1:
        lignes=[]
        with open("enseignats.txt", "r") as f:
            for ligne in f:
                txt=ligne.split("\t")
                if txt[0]!=code:
                    lignes.append(ligne)
                else:
                    lignes.append(code+"\t"+prenom+"\t"+nom+"\t"+matiere+"\n")
        f.close()
        with open("enseignats.txt", "w") as f:
            for l in lignes:
                f.write(l)
        f.close()
        print("Enseignats modifié avec succés")
    else: 
        print("Enseignat "+code+" n'existe pas\n")
def ModifierCour(code,matiere):
    if CourExiste(code)==1:
        lignes=[]
        with open("cours.txt", "r") as f:
            for ligne in f:
                txt=ligne.split("\t")
                if txt[0]!=code:
                    lignes.append(ligne)
                else:
                    lignes.append(code+"\t"+matiere+"\n")
        f.close()
        with open("cours.txt", "w") as f:
            for l in lignes:
                f.write(l)
        f.close()
        print("Cour modifié avec succés")
    else: 
        print("Cour "+code+" n'existe pas\n")
