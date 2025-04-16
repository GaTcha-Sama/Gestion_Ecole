import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root1",
        password="root1",  
        database="ecole"
    )