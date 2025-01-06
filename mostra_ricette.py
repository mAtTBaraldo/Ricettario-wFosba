import mysql.connector

# connessione al database 
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ricettario"
)

cursor = db.cursor()


translations = {
    'en': {

        'name': "Name",
        'type': "Type",
        'ingredients': "Ingredients",
        'procedure': "Procedure",
        'recipe_not_found': "Recipe not found in the recipe book."
    },
    'it': {

        'name': "Nome",
        'type': "Tipo",
        'ingredients': "Ingredienti",
        'procedure': "Procedura",
        'recipe_not_found': "Ricetta non trovata nel ricettario."
    }
}

#mostrare tutte le ricette nel database

def mostra_ricette(lang):
    sql = "SELECT * FROM ricettario"
    cursor.execute(sql)
    risultati = cursor.fetchall()
    
    if risultati:
            
            for record in risultati:
                print(f"\n{translations[lang]['name']}: {record[2]}")
                print(f"{translations[lang]['type']}: {record[1]}")
                ingredienti = record[3].split(',')
                print(f"{translations[lang]['ingredients']}:")
                for ingrediente in ingredienti:
                    print(f" - {ingrediente.strip()}")
                print(f"{translations[lang]['procedure']}: {record[4]}")
                print("================================")
    else:
        print(translations[lang]['recipe_not_found'])