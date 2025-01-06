import mysql.connector

# connessione al database 
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
        'recipe_not_found': "Recipe not found in the recipe book.",
        'new_name': "Enter the new name of the recipe: ",
        'new_type': "Enter the new type of the recipe: ",
        'new_ingredients': "Enter the ingredients of the recipe (separated by commas): ",
        'new_procedure': "Enter the preparation of the recipe: ",
        'recipe_updated': "Recipe updated successfully!",
        'update_error': "An error occurred while updating the recipe: {error}"
    },
    'it': {
        'insert_recipe_name': "Inserisci il nome della ricetta da cercare (scrivi 'quit' o 1 per uscire): ",
        'recipe_found': "Ricetta trovata nel ricettario.",
        'recipe_not_found': "Ricetta non trovata nel ricettario.",
        'new_name': "Inserisci il nuovo nome della ricetta: ",
        'new_type': "Inserisci il nuovo tipo della ricetta: ",
        'new_ingredients': "Inserisci gli ingredienti della ricetta (separati da virgola): ",
        'new_procedure': "Inserisci la preparazione della ricetta: ",
        'recipe_updated': "Ricetta modificata con successo!",
        'update_error': "Si è verificato un errore durante la modifica della ricetta: {error}"
    }
}

# Funzione per modificare una ricetta
def modifica_ricetta(lang):
    nome_ricetta = input(translations[lang]['insert_recipe_name'])
    if nome_ricetta.lower() == "quit" or nome_ricetta.lower() == "1":
        return
    
    cursor.execute("SELECT * FROM `ricettario` WHERE `nome` = %s", (nome_ricetta,))
    risultati = cursor.fetchall()

    if risultati:  
        print(translations[lang]['recipe_found'])
        for record in risultati: 
            print(f"\nNome: {record[2]}")  # Assumendo che il nome sia nella colonna 2
            print(f"Tipo: {record[1]}")  # Assumendo che il tipo sia nella colonna 1
            
            # Assumendo che gli ingredienti siano memorizzati nella colonna 3 come stringa
            ingredienti = record[3].split(',')  # Divide la stringa in una lista
            print("Ingredienti:")
            for ingrediente in ingredienti:
                print(f" - {ingrediente.strip()}")  # Stampa ogni ingrediente, rimuovendo spazi superflui
            
            print(f"Procedura: {record[4]}")  # Assumendo che la procedura sia nella colonna    
    else:
        print(translations[lang]['recipe_not_found'])
        return

    nuovo_nome = input(translations[lang]['new_name'])
    tipo = input(translations[lang]['new_type'])
    ingredienti = input(translations[lang]['new_ingredients'])
    ricetta = input(translations[lang]['new_procedure'])
    
    # Aggiornamento della ricetta nel database
    sql = "UPDATE `ricettario` SET tipo=%s, nome=%s, ingredienti=%s, ricetta=%s WHERE nome=%s"
    values = (tipo, nuovo_nome, ingredienti, ricetta, nome_ricetta)
    
    try:
        cursor.execute(sql, values)
        db.commit()
        print(translations[lang]['recipe_updated'])
    except Exception as e:
        db.rollback()
        print(translations[lang]['update_error'].format(error=str(e)))


