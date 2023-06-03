import sqlite3

from Topics import get_dbinfo_from_topic

cursor: sqlite3.Cursor = None

def init_database_connection():
    """
    Initialise une connection avec la base de donnée.
    """

    connection = sqlite3.connect("Web/domo/src/domo")
    cursor     = connection.cursor()

def push_to_database(topic: str, value: str):
    """
    Envoie en base de donnée. La request SQL varie en fonction du topic sur 
    lequel une valeur est recue.

    Attention une connection avec la base de donnée doit d'abord etre ouverte
    avec la fonction init_database_connection() .
    """

    dbLoc = get_dbinfo_from_topic(topic)
    table = dbLoc["table"]
    type  = dbLoc["type"]

    if(table == "donnees_actuelles"):
        cursor.execute('''
        UPDATE ''' + table + '''
        SET valeur=''' + value + '''
        WHERE type_de_donnees = ''' + type + '''
        ''')

    elif(table == "historique"):
        cursor.execute('''
        INSERT INTO historique (type_de_donnees, valeur)
        VALUES (''' + type + ''', ''' + value + ''')
        ''')