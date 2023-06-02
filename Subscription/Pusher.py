import sqlite3

cursor: sqlite3.Cursor = None

dbID = {
    "Maison/Ventilateur/Mode":["donnees_actuelles", "ventilateur_mode"],
    "Maison/Ventilateur/Actif":["donnees_actuelles","ventilateur_ctrl"],
    "Maison/Ventilateur/Ctrl":["donnees_actuelles","ventilateur_actif"],
    "Maison/Temperature":["historique","temperature"],
    "Maison/Humidite":["historique","humidite"],
}

def init_database_connection():
    """
    Initialise une connection avec la base de donnée
    """

    connection = sqlite3.connect("Web/domo/src/domo")
    cursor     = connection.cursor()

def push_to_database(topic: str, value: str):
    """
    Update en base de donnée
    """
    where = dbID[topic]
    table = where[0]
    type  = where[1]

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