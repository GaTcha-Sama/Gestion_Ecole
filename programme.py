from database import get_connection

########### TABLE PROGRAMME ###############

# 1️-Insertion d'un programme
def insert_programme(id_programme, id_matiere, id_classe, id_prof, annee):
    conn = get_connection()
    cursor = conn.cursor()
    req="INSERT INTO Programme (id_programme, id_matiere, id_classe, id_prof, annee) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(req,(id_programme, id_matiere, id_classe, id_prof, annee))
    conn.commit()
    print("Programme ajouté.")
    cursor.close()
    conn.close()

# 2️- Suppression d’un programme
def delete_programme(id_programme):
    conn = get_connection()
    cursor = conn.cursor()
    req="DELETE FROM Programme WHERE id_programme = %s"
    cursor.execute(req,(id_programme,))
    conn.commit()
    print(f"Programme {id_programme} supprimé.")
    cursor.close()
    conn.close()

# 3️- Mise à jour d’un programme
def update_programme(id_programme, id_matiere, id_classe, id_prof, annee):
    conn = get_connection()
    cursor = conn.cursor()
    req="UPDATE Programme SET id_matiere = %s, id_classe = %s, id_prof = %s, annee = %s WHERE id_programme = %s"
    cursor.execute(req,(id_matiere, id_classe, id_prof, annee, id_programme))
    conn.commit()
    print(f"Programme {id_programme} mis à jour.")
    cursor.close()
    conn.close()

# 4️- Afficher tous les programmes
def get_all_programmes():
    conn = get_connection()
    cursor = conn.cursor()
    req="SELECT * FROM Programme"
    cursor.execute(req)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()














