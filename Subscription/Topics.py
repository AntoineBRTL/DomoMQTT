# Tout les topics sont dans ce fichier

def get_topics():
    '''Renvois la liste de topics renseignés dans le programme.'''
    return list(topicDbInfo.keys())

def get_dbinfo_from_topic(topic: str):
    '''Renvois des informations utiles pour la base de donnée en fonction du topic donné.'''

    return topicDbInfo[topic]

topicDbInfo = {

    "Maison/Ventilateur/Mode":
    {
        "table":"donnees_actuelles", 
        "type":"ventilateur_mode"
    },

    "Maison/Ventilateur/Actif":
    {
        "table":"donnees_actuelles", 
        "type":"ventilateur_ctrl"
    },

    "Maison/Ventilateur/Ctrl":
    {
        "table":"donnees_actuelles", 
        "type":"ventilateur_actif"
    },
    

    "Maison/Temperature":
    {
        "table":"historique", 
        "type":"temperature"
    },

    "Maison/Humidite":
    {
        "table":"historique", 
        "type":"humidite"
    },
}