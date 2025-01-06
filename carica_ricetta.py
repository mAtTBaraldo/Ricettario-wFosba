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

tipi = ["antipasto", "primo", "contorno", "secondo", "dessert", "appetizer", "first course", "second course", "side dish", "dessert"]

# Dizionario delle traduzioni
translations = {
    'en': {
        'enter_recipe_name': "Enter the name of the recipe (type 'quit' or 1 to exit): ",
        'recipe_exists': "The recipe already exists in the recipe book.",
        'enter_recipe_type': "Enter the type of the recipe (e.g. appetizer, first course, second course, side dish, dessert): ",
        'invalid_type': "Invalid type. Please try again.",
        'enter_ingredients': "Enter the ingredients for the recipe (separated by commas): ",
        'enter_procedure': "Enter the procedure for the recipe: ",
        'success': "Recipe added successfully!"
    },
    'it': {
        'enter_recipe_name': "Inserisci il nome della ricetta (scrivi 'quit' o 1 per uscire): ",
        'recipe_exists': "La ricetta esiste già nel ricettario.",
        'enter_recipe_type': "Inserisci il tipo della ricetta (es. antipasto, primo, secondo, contorno, dessert): ",
        'invalid_type': "Tipo non valido. Riprova.",
        'enter_ingredients': "Inserisci gli ingredienti della ricetta (separati da virgole): ",
        'enter_procedure': "Inserisci la procedura della ricetta: ",
        'success': "Ricetta aggiunta con successo!"
    }
}

def carica_ricetta(lang):
    while True:
        # Chiedi all'utente di inserire il nome della ricetta
        nome_ricetta = input(translations[lang]['enter_recipe_name'])
        if nome_ricetta.lower() == "quit" or nome_ricetta == "1":
            break
        
        # Controllo se la ricetta esiste già nel databese
        cursor.execute("SELECT * FROM ricettario WHERE nome = %s", (nome_ricetta,))
        risultati = cursor.fetchall()

        if risultati:  # Se ci sono risultati, vuol dire che la ricetta esiste già
            print(translations[lang]['recipe_exists'])
        else:
            # Creazione record
            sql = "INSERT INTO ricettario (tipo, nome, ingredienti, ricetta) VALUES (%s, %s, %s, %s)"
            while True:
                tipo = input(translations[lang]['enter_recipe_type']) 
                if tipo not in tipi:
                    print(translations[lang]['invalid_type'])
                else:
                    break
            
            ingredienti = input(translations[lang]['enter_ingredients'])
            ricetta = input(translations[lang]['enter_procedure'])
            
            values = (tipo, nome_ricetta, ingredienti, ricetta)
            cursor.execute(sql, values)
            db.commit()
            print(translations[lang]['success'])