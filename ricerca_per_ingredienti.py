import mysql.connector

# Connessione a un database 
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ricettario"
)

# Collegamento cursore 
cursor = db.cursor()

# Dizionario delle traduzioni
translations = {
    'en': {
        'input_ingredients': "\nEnter the ingredients separated by commas: (type 'quit' or 1 to exit) ",
        'recipes_found': "\nRecipes found:",
        'no_recipes_found': "No recipes found."
    },
    'it': {
        'input_ingredients': "\nInserisci gli ingredienti separati da virgola: (scrivi 'quit' o 1 per uscire) ",
        'recipes_found': "\nRicette trovate:",
        'no_recipes_found': "Nessuna ricetta trovata."
    }
}

def ricerca_per_ingredienti(lang):
    while True:
        array_ingredienti = []
        ingredienti = input(translations[lang]['input_ingredients']).split(",")
        if ingredienti[0].lower() == "quit" or ingredienti[0] == "1":
            break
        # Rimuovi spazi bianchi e crea pattern di ricerca
        for i in ingredienti:
            array_ingredienti.append(f"%{i.strip()}%")
        # Prepara la query
        sql = "SELECT * FROM `ricettario` WHERE " + " AND ".join(["ingredienti LIKE %s"] * len(array_ingredienti))
        
        # Esegui la query con i parametri
        cursor.execute(sql, array_ingredienti)
        
        risultati = cursor.fetchall()
        
        if risultati:
            print(translations[lang]['recipes_found'])
            for record in risultati:
                print(f"- Nome: {record[2]}")
                print(f"- Tipo: {record[1]}")
                print("================================")
        else:
            print(translations[lang]['no_recipes_found'])