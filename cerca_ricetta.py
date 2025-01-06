import mysql.connector

# Connessione al database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ricettario"
)

cursor = db.cursor()

# Dizionario delle traduzioni
translations = {
    'en': {
        'insert_recipe_name': "Enter the name of the recipe to search for (type 'quit' or 1 to exit): ",
        'recipe_found': "Recipe found in the recipe book.",
        'name': "Name",
        'type': "Type",
        'ingredients': "Ingredients",
        'procedure': "Procedure",
        'recipe_not_found': "Recipe not found in the recipe book."
    },
    'it': {
        'insert_recipe_name': "Inserisci il nome della ricetta da cercare (scrivi 'quit' o 1 per uscire): ",
        'recipe_found': "Ricetta trovata nel ricettario.",
        'name': "Nome",
        'type': "Tipo",
        'ingredients': "Ingredienti",
        'procedure': "Procedura",
        'recipe_not_found': "Ricetta non trovata nel ricettario."
    }
}

def ricerca_ricetta(lang):
    while True:
        nome_ricetta = input(translations[lang]['insert_recipe_name'])
        if nome_ricetta.lower() == "quit" or nome_ricetta.lower() == "1" or nome_ricetta == " ":
            break
        
        cursor.execute("SELECT * FROM ricettario WHERE nome = %s", (nome_ricetta,))
        risultati = cursor.fetchall()
        
        if risultati:
            print(translations[lang]['recipe_found'])
            for record in risultati:
                print(f"\n{translations[lang]['name']}: {record[2]}")
                print(f"{translations[lang]['type']}: {record[1]}")
                ingredienti = record[3].split(',')
                print(f"{translations[lang]['ingredients']}:")
                for ingrediente in ingredienti:
                    print(f" - {ingrediente.strip()}")
                print(f"{translations[lang]['procedure']}: {record[4]}")
        else:
            print(translations[lang]['recipe_not_found'])