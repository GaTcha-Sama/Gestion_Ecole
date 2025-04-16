from database import get_connection

############### TABLE MATIERE ##############

# 1️-Insertion d'une matière
def insert_matiere(nom_matiere, code_matiere):
    conn = get_connection()
    cursor = conn.cursor()
    req="INSERT INTO Matiere (nom_matiere, code_matiere)VALUES (%s, %s)"
    cursor.execute(req,(nom_matiere, code_matiere))
    conn.commit()
    print("Matière ajouté.")
    cursor.close()
    conn.close()
    
# 2️- Suppression d’une matière
def delete_matiere(id_matiere):
    conn = get_connection()
    cursor = conn.cursor()
    req="DELETE FROM Matiere WHERE id_matiere = %s"
    cursor.execute(req,(id_matiere,))
    conn.commit()
    print(f"Matière {id_matiere} supprimé.")
    cursor.close()
    conn.close()    
    
# 3️- Mise à jour d’une matière
def update_matiere(id_matiere, nom_matiere, code_matiere):
    conn = get_connection()
    cursor = conn.cursor()
    req="UPDATE Matiere SET nom_matiere = %s, code_matiere = %s WHERE id_matiere = %s"
    cursor.execute(req,(nom_matiere, code_matiere, id_matiere))
    conn.commit()
    print(f"Matière {id_matiere} mis à jour.")
    cursor.close()
    conn.close()
    
# 4️- Afficher toutes les matières
def get_all_matieres(): 
    conn = get_connection()
    cursor = conn.cursor()
    req="SELECT * FROM Matiere"
    cursor.execute(req)
    rows = cursor.fetchall()
    for row in rows:
        print(row)  
    cursor.close()
    conn.close()
    
