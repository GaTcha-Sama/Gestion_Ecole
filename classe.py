from database import get_connection

############### TABLE CLASSE ##############

# 1️-Insertion d'une classe
def insert_classe(code_classe, nom_classe):
    conn = get_connection()
    cursor = conn.cursor()
    req="INSERT INTO Classe (code_classe, nom_classe)VALUES (%s, %s)"
    cursor.execute(req,(code_classe, nom_classe))
    conn.commit()
    print("Classe ajouté.")
    cursor.close()
    conn.close()

# 2️- Suppression d’une classe
def delete_classe(id_classe):
    conn = get_connection()
    cursor = conn.cursor()
    req="DELETE FROM Classe WHERE id_classe = %s"
    cursor.execute(req,(id_classe,))
    conn.commit()
    print(f"Classe {id_classe} supprimé.")
    cursor.close()
    conn.close()

# 3️- Mise à jour d’une classe
def update_classe(id_classe, code_classe, nom_classe):
    conn = get_connection()
    cursor = conn.cursor()
    req="UPDATE Classe SET code_classe = %s, nom_classe = %s WHERE id_classe = %s"
    cursor.execute(req,(code_classe, nom_classe, id_classe))
    conn.commit()
    print(f"Classe {id_classe} mis à jour.")
    cursor.close()
    conn.close()

# 4️- Afficher toutes les classes
def get_all_classes():
    conn = get_connection()
    cursor = conn.cursor()
    req="SELECT * FROM Classe"
    cursor.execute(req)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()
