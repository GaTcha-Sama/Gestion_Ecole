import inscription
import professeur
import eleve
import matiere
import classe
import programme
import notes

def main():
    print("Bienvenue dans le programme de gestion de l'école")
    while True:
        print("1. Gestion des élèves")
        print("2. Gestion des matières")
        print("3. Gestion des classes")
        print("4. Gestion des programmes")
        print("5. Gestion des notes")
        print("6. Gestion des professeurs")
        print("7. Gestion des inscriptions")
        print("8. Quitter")
        choix = input("Entrez votre choix: ")
        
        match choix:
            case "1":
                print("1. Afficher tous les élèves")
                print("2. Insérer un élève")
                print("3. Supprimer un élève")
                print("4. Mettre à jour un élève")
                print("5. Voir la moyenne de l'élève")
                print("6. Voir l'ordre des élèves par moyenne générale")
                choix_eleve = input("Entrez votre choix: ")
                if choix_eleve == "1":
                    eleve.get_all_eleves()
                elif choix_eleve == "2":
                    print("Entrez le nom de l'élève: ")
                    nom = input()
                    print("Entrez l'adresse de l'élève: ")
                    adresse = input()
                    print("Entrez la date de naissance de l'élève: ")
                    date_naissance = input()
                    eleve.insert_eleve(nom, date_naissance, adresse) 
                elif choix_eleve == "3":
                    print("Supprimer un élève")
                    print("Entrez l'identifiant de l'élève: ")
                    id = input()
                    eleve.delete_eleve(id)
                elif choix_eleve == "4":
                    print("Mettre à jour un élève")
                    print("Entrez l'identifiant de l'élève: ")
                    eleve.get_all_eleves()
                    id = input()
                    print("Entrez le nom de l'élève: ")
                    nom = input()
                    print("Entrez la date de naissance de l'élève: ")
                    date_naissance = input()
                    print("Entrez l'adresse de l'élève: ")
                    adresse = input()
                    eleve.update_eleve(id, nom, date_naissance, adresse)
                elif choix_eleve == "5":
                    print("Entrez l'identifiant de l'élève: ")
                    id = input()
                    eleve.get_moyenne_eleve(id)
                elif choix_eleve == "6":                    
                    eleve.get_eleves_par_moyenne()
            case "2":
                print("1. Afficher toutes les matières")
                print("2. Insérer une matière")
                print("3. Supprimer une matière")
                print("4. Mettre à jour une matière")
                choix_matiere = input("Entrez votre choix: ")
                if choix_matiere == "1":
                    matiere.get_all_matieres()
                elif choix_matiere == "2":
                    print("Entrez le code de la matière: ")
                    code = input()
                    print("Entrez le nom de la matière: ")
                    nom = input()
                    matiere.insert_matiere(code, nom)
                elif choix_matiere == "3":
                    print("Entrez l'identifiant de la matière: ")
                    id = input()
                    matiere.delete_matiere(id)
                elif choix_matiere == "4":
                    print("Entrez l'identifiant de la matière: ")
                    id = input()
                    print("Entrez le code de la matière: ")
                    code = input()
                    print("Entrez le nom de la matière: ")
                    nom = input()
                    matiere.update_matiere(id, code, nom)
            case "3":
                print("1. Afficher toutes les classes")
                print("2. Insérer une classe")
                print("3. Supprimer une classe")
                print("4. Mettre à jour une classe")
                choix_classe = input("Entrez votre choix: ")
                if choix_classe == "1":
                    classe.get_all_classes()
                elif choix_classe == "2":
                    print("Entrez le code de la classe: ")
                    code = input()
                    print("Entrez le nom de la classe: ")
                    nom = input()
                    classe.insert_classe(code, nom)
                elif choix_classe == "3":
                    print("Entrez l'identifiant de la classe: ")
                    id = input()
                    classe.delete_classe(id)
                elif choix_classe == "4":
                    print("Entrez l'identifiant de la classe: ")
                    id = input()
                    print("Entrez le code de la classe: ")
                    code = input()
                    print("Entrez le nom de la classe: ")
                    nom = input()
                    classe.update_classe(id, code, nom)
            case "4":
                print("1. Afficher tous les programmes")
                print("2. Insérer un programme")
                print("3. Supprimer un programme")
                print("4. Mettre à jour un programme")
                choix_programme = input("Entrez votre choix: ")
                if choix_programme == "1":
                    programme.get_all_programmes()
                elif choix_programme == "2":
                    print("Entrez l'identifiant du programme: ")
                    id = input()
                    print("Entrez l'identifiant de la matière: ")
                    id_matiere = input()
                    print("Entrez l'identifiant de la classe: ")
                    id_classe = input()
                    print("Entrez l'identifiant du professeur: ")
                    id_prof = input()
                    print("Entrez l'année: ")
                    annee = input()
                    programme.insert_programme(id, id_matiere, id_classe, id_prof, annee)
                elif choix_programme == "3":
                    print("Entrez l'identifiant du programme: ")
                    id = input()
                    programme.delete_programme(id)
                elif choix_programme == "4":
                    print("Entrez l'identifiant du programme: ")
                    id = input()
                    print("Entrez l'identifiant de la matière: ")
                    id_matiere = input()
                    print("Entrez l'identifiant de la classe: ")
                    id_classe = input()
                    print("Entrez l'identifiant du professeur: ")
                    id_prof = input()
                    programme.update_programme(id, id_matiere, id_classe, id_prof, annee)
            case "5":
                print("1. Afficher toutes les notes")
                print("2. Insérer une note à un élève")
                print("3. Supprimer une note")
                print("4. Mettre à jour une note")
                choix_notation = input("Entrez votre choix: ")
                if choix_notation == "1":
                    notes.get_all_notes()
                elif choix_notation == "2":
                    print("Entrez l'identifiant de l'élève: ")
                    eleve.get_all_eleves()
                    id_eleve = input()
                    print("Entrez l'identifiant de la matière: ")
                    matiere.get_all_matieres()
                    id_matiere = input()
                    print("Entrez l'année: ")
                    annee = input()
                    print("Entrez la session: ")
                    print("1. 1er trimestre")
                    print("2. 2eme trimestre")
                    print("3. 3eme trimestre")
                    sessions = input()
                    print("Entrez la note: ")
                    note = input()
                    notes.insert_note(id_eleve, id_matiere, annee, sessions, note)
                elif choix_notation == "3":
                    print("Entrez l'identifiant de la note: ")
                    id = input()
                    notes.delete_note(id)
                elif choix_notation == "4":
                    print("Entrez l'identifiant de la note: ")
                    id = input()
                    print("Entrez la note: ")
                    note = input()
                    notes.update_note(id, id_matiere, annee, note)
            case "6":
                print("1. Afficher tous les professeurs")
                print("2. Insérer un professeur")
                print("3. Supprimer un professeur")
                print("4. Mettre à jour un professeur")
                choix_professeur = input("Entrez votre choix: ")
                if choix_professeur == "1":                    
                    professeur.get_all_professeurs()
                elif choix_professeur == "2":
                    print("Entrez le nom du professeur: ")
                    nom = input()
                    print("Entrez l'adresse du professeur: ")
                    adresse = input()
                    professeur.insert_professeur(nom, adresse)
                elif choix_professeur == "3":
                    professeur.delete_professeur()
                elif choix_professeur == "4":
                    print("Entrez l'identifiant du professeur: ")
                    id = input()
                    print("Entrez le nom du professeur: ")
                    nom = input()
                    print("Entrez l'adresse du professeur: ")
                    adresse = input()
                    professeur.update_professeur(id, nom, adresse)
            case "7":
                print("1. Afficher toutes les inscriptions")
                print("2. Insérer une inscription")
                print("3. Supprimer une inscription")
                print("4. Mettre à jour une inscription")
                choix_inscription = input("Entrez votre choix: ")
                if choix_inscription == "1":
                    inscription.get_all_inscriptions()
                elif choix_inscription == "2":
                    print("Entrez l'identifiant de l'inscription: ")
                    id = input()
                    print("Entrez l'identifiant de l'élève: ")
                    id_eleve = input()
                    print("Entrez l'identifiant de la classe: ")
                    id_classe = input()
                    print("Entrez l'année: ")
                    annee = input()
                    inscription.insert_inscription(id, id_eleve, id_classe, annee)
                elif choix_inscription == "3":
                    print("Entrez l'identifiant de l'inscription: ")
                    id = input()
                    inscription.delete_inscription(id)
                elif choix_inscription == "4":
                    print("Entrez l'identifiant de l'inscription: ")
                    id = input()
                    print("Entrez l'identifiant de l'élève: ")
                    inscription.update_inscription()
            case "8":
                print("Au revoir et à bientôt !")
                break
            case _:
                print("Choix invalide")

if __name__ == "__main__":
    main()

