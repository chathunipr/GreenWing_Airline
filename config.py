import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3307,
        user="root",
        password="12345678",
        database="greenwing"
    )
    return connection