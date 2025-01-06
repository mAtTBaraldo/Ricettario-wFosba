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
        'enter_ingredient': "Enter the ingredient to search for (type 'quit' or 1 to exit): ",
        'no_recipes_found': "No recipes found for the ingredient '{}'.",
        'recipes_found': "Recipes found for the ingredient '{}':",
        'recipe_name': "- Name: {}",
        'recipe_type': "- Type: {}"
    },
    'it': {
        'enter_ingredient': "Inserisci l'ingrediente da cercare (scrivi 'quit' o 1 per uscire): ",
        'no_recipes_found': "Nessuna ricetta trovata per l'ingrediente '{}'.",
        'recipes_found': "Ricette trovate per l'ingrediente '{}':",
        'recipe_name': "- Nome: {}",
        'recipe_type': "- Tipo: {}"
    }
}

# ricerca per ingrediente 
def ricerca_per_ingrediente(lang):
    while True:
        ingrediente = input(translations[lang]['enter_ingredient'])
        if ingrediente.lower() == "quit" or ingrediente == "1":
            break
        elif ingrediente.lower() == " ":
            print(translations[lang]['no_recipes_found'].format(" "))
            continue
        cursor.execute("SELECT * FROM `ricettario` WHERE `ingredienti` LIKE %s", (f"%{ingrediente}%",))
        risultati = cursor.fetchall()
        
        if risultati:
            print(translations[lang]['recipes_found'].format(ingrediente))
            for record in risultati:
                print(translations[lang]['recipe_name'].format(record[2]))
                print(translations[lang]['recipe_type'].format(record[1]))
                print("================================")
        else:
            print(translations[lang]['no_recipes_found'].format(ingrediente))
