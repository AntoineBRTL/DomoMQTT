import sqlite3

cursor: sqlite3.Cursor

def init_database_connection():
    """
    Initialise une connection avec la base de donnée
    """

    connection = sqlite3.connect("./DomoDB/domo.db")
    cursor     = connection.cursor()

def push_to_database(topic: str, value: str):
    """
    Stock une publication en base de donnée
    """
    #cursor.execute("INSERT INTO DonneeActuelles VALUES ()")
    print(topic, value)