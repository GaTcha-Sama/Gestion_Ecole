from database import get_connection

############### TABLE ELEVE ##############

# 1️-Insertion d'un élève
def insert_eleve(nom, date_naissance, adresse):
    conn = get_connection()
    cursor = conn.cursor()
    req="INSERT INTO Eleve (nom, date_naissance, adresse)VALUES (%s, %s, %s)"
    cursor.execute(req,(nom, date_naissance, adresse))
    conn.commit()
    print("Élève ajouté.")
    cursor.close()
    conn.close()

# 2️- Suppression d'un élève
def delete_eleve(id_eleve):
    conn = get_connection()
    cursor = conn.cursor()
    req="DELETE FROM Eleve WHERE id_eleve = %s"
    cursor.execute(req,(id_eleve,))
    conn.commit()
    print(f"Élève {id_eleve} supprimé.")
    cursor.close()
    conn.close()

# 3️- Mise à jour d'un élève
def update_eleve(id_eleve, nom, date_naissance, adresse):
    conn = get_connection()
    cursor = conn.cursor()
    req="UPDATE Eleve SET nom = %s, date_naissance = %s, adresse = %s WHERE id_eleve = %s"
    cursor.execute(req,(nom, date_naissance, adresse, id_eleve))
    conn.commit()
    print(f"Élève {id_eleve} mis à jour.")
    cursor.close()
    conn.close()

# 4️- Afficher tous les élèves
def get_all_eleves():
    conn = get_connection()
    cursor = conn.cursor()
    req="SELECT * FROM Eleve"
    cursor.execute(req)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()
    
# 5️- Afficher la moyenne d'un élève
def get_moyenne_eleve(id_eleve):
    conn = get_connection()
    cursor = conn.cursor()
    req="SELECT AVG(note) FROM Note WHERE id_eleve = %s"
    cursor.execute(req,(id_eleve,))
    moyenne = cursor.fetchone()[0]
    if moyenne is None:
        print(f"L'élève {id_eleve} n'a pas encore de notes enregistrées.")
    else:
        print("-------------------------------------------")
        print(f"La moyenne de l'élève {id_eleve} est {moyenne:.2f}")
        print("-------------------------------------------")
    cursor.close()
    conn.close()
    
# 6️- Afficher l'ordre des élèves par moyenne générale   
def get_eleves_par_moyenne():
    conn = get_connection()
    cursor = conn.cursor()
    req = """
        SELECT e.nom, AVG(n.note) as moyenne 
        FROM Eleve e 
        JOIN Note n ON e.id_eleve = n.id_eleve 
        GROUP BY e.id_eleve, e.nom 
        ORDER BY moyenne DESC
    """
    cursor.execute(req)
    rows = cursor.fetchall()
    print("\nClassement des élèves par moyenne générale :")
    print("-------------------------------------------")
    for i, row in enumerate(rows, 1):
        print(f"{i}. {row[0]} - Moyenne : {row[1]:.2f}")
    print("-------------------------------------------")
    cursor.close()
    conn.close()
