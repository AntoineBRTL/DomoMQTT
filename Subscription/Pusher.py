import sqlite3

cursor: sqlite3.Cursor

def initDBConnection():

    connection = sqlite3.connect("./DomoDB/domo.db")
    cursor     = connection.cursor()

# Contient des fonctions utiles pour l'envoie en base de donnée

# Cette fonction envoie une valeur en base de donnée
def pushToDB(topic: str, value: bytes):

    decodedValue: str = value.decode()

    #cursor.execute("INSERT INTO DonneeActuelles VALUES ()")
    print(topic, decodedValue)