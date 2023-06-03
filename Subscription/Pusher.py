import sqlite3

from Topics import get_dbinfo_from_topic

connection = sqlite3.connect("Web/domo/src/domo/domo_dev.db")
cursor: sqlite3.Cursor = connection.cursor()

def push_to_database(topic: str, value: str):
    """
    Envoie en base de donnée. La request SQL varie en fonction du topic sur 
    lequel une valeur est recue.
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
        VALUES (' ''' + type + ''' ', ''' + value + ''')
        ''')