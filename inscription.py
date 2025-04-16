from database import get_connection

############### TABLE INSCRIPTION   ##############

# 1️-Insertion d'une inscription
def insert_inscription(id_inscription, id_eleve, id_classe, annee):
    conn = get_connection()
    cursor = conn.cursor()
    req="INSERT INTO Inscription (id_inscription, id_eleve, id_classe, annee) VALUES (%s, %s, %s, %s)"
    cursor.execute(req,(id_inscription, id_eleve, id_classe, annee))
    conn.commit()
    print("Inscription ajouté.")
    cursor.close()
    conn.close()
    
# 2️- Suppression d’une inscription
def delete_inscription(id_inscription):
    conn = get_connection()
    cursor = conn.cursor()
    req="DELETE FROM Inscription WHERE id_inscription = %s"
    cursor.execute(req,(id_inscription,))
    conn.commit()
    print(f"Inscription {id_inscription} supprimé.")
    cursor.close()
    conn.close()
    
# 3️- Mise à jour d’une inscription
def update_inscription(id_inscription, id_eleve, id_classe, annee):
    conn = get_connection()
    cursor = conn.cursor()
    req="UPDATE Inscription SET id_eleve = %s, id_classe = %s, annee = %s WHERE id_inscription = %s"
    cursor.execute(req,(id_eleve, id_classe, annee, id_inscription))
    conn.commit()
    print(f"Inscription {id_inscription} mis à jour.")
    cursor.close()
    conn.close()    
    
# 4️- Afficher toutes les inscriptions
def get_all_inscriptions():
    conn = get_connection()
    cursor = conn.cursor()
    req="SELECT * FROM Inscription"
    cursor.execute(req) 
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()    


