import mysql.connector

# connessione al database 
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ricettario"
)

# collegamento cursore 
cursor = db.cursor()

# Dizionario delle traduzioni
translations = {
    'en': {
        'insert_recipe_name': "Enter the name of the recipe to search for (type 'quit' or 1 to exit): ",
        'recipe_deleted': "Recipe '{recipe_name}' successfully deleted.",
        'recipe_not_found': "Recipe not found in the recipe book."
    },
    'it': {
        'insert_recipe_name': "Inserisci il nome della ricetta da cercare (scrivi 'quit' o 1 per uscire): ",
        'recipe_deleted': "Ricetta '{recipe_name}' eliminata con successo.",
        'recipe_not_found': "Ricetta non trovata nel ricettario."
    }
}

def elimina_ricetta(lang):
    while True:
        nome_ricetta = input(translations[lang]['insert_recipe_name'])
        if nome_ricetta.lower() == "quit" or nome_ricetta == "1":
            break

        cursor.execute("SELECT * FROM ricettario WHERE nome = %s", (nome_ricetta,))
        risultati = cursor.fetchall()
        if risultati:
            cursor.execute("DELETE FROM ricettario WHERE nome = %s", (nome_ricetta,))
            db.commit()
            print(translations[lang]['recipe_deleted'].format(recipe_name=nome_ricetta))
            break
        else:
            print(translations[lang]['recipe_not_found'])