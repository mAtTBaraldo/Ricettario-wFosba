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

tipi = ["antipasto", "primo", "secondo", "dessert"]

def carica_ricetta():
    while True:
        # Chiedi all'utente di inserire il nome della ricetta
        nome_ricetta = input("Inserisci il nome della ricetta (scrivi 'quit' o 1 per uscire): ")
        if nome_ricetta.lower() == "quit" or nome_ricetta == "1":
            break
        
        # Controllo se la ricetta esiste già nel databese
        cursor.execute("SELECT * FROM ricettario WHERE nome = %s", (nome_ricetta,))
        risultati = cursor.fetchall()

        if risultati:  # Se ci sono risultati, vuol dire che la ricetta esiste già
            print("La ricetta esiste già nel ricettario.")
        else:
            # Creazione record
            sql = "INSERT INTO ricettario (tipo, nome, ingredienti, ricetta) VALUES (%s, %s, %s, %s)"  # Creazione delle colonne e caricamento di esse
            while True:
                tipo = input("Inserisci il tipo della ricetta (es. antipasto, primo, secondo, dessert): ") 
                if tipo not in tipi:
                    print("Tipo non valido. Riprova.")
                else:
                    break
            
            ingredienti = input("Inserisci gli ingredienti della ricetta (separati da virgole): ")
            ricetta = input("Inserisci la procedura della ricetta: ")
            
            values = (tipo, nome_ricetta, ingredienti, ricetta)
            cursor.execute(sql, values)
            db.commit()
            print("Ricetta aggiunta con successo!")