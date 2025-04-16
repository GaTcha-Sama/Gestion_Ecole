from database import get_connection

############### TABLE NOTES ##############

# 1️-Insertion d'une note
def insert_note(id_eleve, id_matiere, annee, sessions, note):
    conn = get_connection()
    cursor = conn.cursor()
    req = "INSERT INTO Note (id_eleve, id_matiere, annee, sessions, note)VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(req, (id_eleve, id_matiere, annee, sessions, note))
    conn.commit()
    print("Note ajoutée.")
    cursor.close()
    conn.close()
    
# 2️- Suppression d'une note
def delete_note(id_note):
    conn = get_connection()
    cursor = conn.cursor()
    req="DELETE FROM Note WHERE id_note = %s"
    cursor.execute(req,(id_note,))
    conn.commit()
    print(f"Note {id_note} supprimé.")
    cursor.close()
    conn.close()
    
# 3️- Mise à jour d'une note
def update_note(id_note, id_eleve, id_matiere, annee, sessions, note):
    conn = get_connection()
    cursor = conn.cursor()
    req="UPDATE Note SET id_eleve = %s, id_matiere = %s, annee = %s, sessions = %s, note = %s WHERE id_note = %s"
    cursor.execute(req,(id_eleve, id_matiere, annee, sessions, note, id_note))
    conn.commit()
    print(f"Note {id_note} mis à jour.")
    cursor.close()
    conn.close()
    
# 4️- Afficher toutes les notes
def get_all_notes():
    conn = get_connection()
    cursor = conn.cursor()
    req="SELECT * FROM Note"
    cursor.execute(req)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()     

