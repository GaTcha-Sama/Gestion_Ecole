from database import get_connection

############### TABLE PROFESSEUR ##############

# 1️-Insertion d'un professeur
def insert_professeur(nom, adresse):
    conn = get_connection()
    cursor = conn.cursor()
    req="INSERT INTO Professeur (nom, adresse)VALUES (%s, %s)"
    cursor.execute(req,(nom, adresse))
    conn.commit()
    print("Professeur ajouté.")
    cursor.close()
    conn.close()

# 2️- Suppression d’un professeur
def delete_professeur(id_prof):
    conn = get_connection()
    cursor = conn.cursor()
    req="DELETE FROM Professeur WHERE id_prof = %s"
    cursor.execute(req,(id_prof,))
    conn.commit()
    print(f"Professeur {id_prof} supprimé.")
    cursor.close()
    conn.close()

# 3️- Mise à jour d’un professeur
def update_professeur(id_prof, nom, adresse):
    conn = get_connection()
    cursor = conn.cursor()
    req="UPDATE Professeur SET nom = %s, adresse = %s WHERE id_prof = %s"
    cursor.execute(req,(nom, adresse, id_prof))
    conn.commit()
    print(f"Professeur {id_prof} mis à jour.")
    cursor.close()
    conn.close()

# 4️- Afficher tous les professeurs
def get_all_professeurs():
    conn = get_connection()
    cursor = conn.cursor()
    req="SELECT * FROM Professeur"
    cursor.execute(req)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()
    
