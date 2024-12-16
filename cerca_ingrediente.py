import mysql.connector

#connessione ad un database 
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "ricettario"
)

#collegamento cursore 
cursor = db.cursor()

#ricerca per ingrediente 
def ricerca_per_ingrediente():
    while True:
        ingrediente = input("Inserisci l'ingrediente da cercare (scrivi 'quit' o 1 per uscire): ")
        if ingrediente.lower() == "quit" or ingrediente == "1":
            break
        
        cursor.execute("SELECT * FROM `ricettario` WHERE `ingredienti` LIKE %s", (f"%{ingrediente}%",))
        risultati = cursor.fetchall()
        
        if risultati:
            print(f"Ricette trovate per l'ingrediente '{ingrediente}':")
            for record in risultati:
                print(f"- Nome: {record[2]}")
                print(f"- Tipo: {record[1]}")
                print("================================")
        else:
                print(f"Nessuna ricetta trovata per l'ingrediente '{ingrediente}'.")
