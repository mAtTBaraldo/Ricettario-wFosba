import mysql.connector

#connessione ad un database 
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "ricettario"
)
cursor = db.cursor()
def ricerca_ricetta():
    while True:
        nome_ricetta = input("Inserisci il nome della ricetta da cercare (scrivi 'quit' per uscire): ")
        if nome_ricetta.lower() == "quit" or nome_ricetta == "1":
            break
        
        cursor.execute("SELECT * FROM `ricettario` WHERE `nome` = %s", (nome_ricetta,))
        risultati = cursor.fetchall()

        if risultati:  
            print("Ricetta trovata nel ricettario.")
            for record in risultati: 
                print(f"\nNome: {record[2]}")  # Assumendo che il nome sia nella colonna 2
                print(f"Tipo: {record[1]}")  # Assumendo che il tipo sia nella colonna 1
                
                # Assumendo che gli ingredienti siano memorizzati nella colonna 3 come stringa
                ingredienti = record[3].split(',')  # Divide la stringa in una lista
                print("Ingredienti:")
                for ingrediente in ingredienti:
                    print(f" - {ingrediente.strip()}")  # Stampa ogni ingrediente, rimuovendo spazi superflui
                
                print(f"Procedura: {record[4]}")  # Assumendo che la procedura sia nella colonna 4
        else:
            print("Ricetta non trovata nel ricettario.")