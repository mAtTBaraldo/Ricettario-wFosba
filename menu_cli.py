import time
from carica_ricetta import carica_ricetta
from stampa_ricetta import ricerca_ricetta
from cerca_ingrediente import ricerca_per_ingrediente

def menu():
    funzioni = [
        {
            "nome": "aggiungi ricetta",
            "funzione_help": ' Per aggiungere una nuova ricetta al ricettario',
            "funzione": 'è stata scelta la funzione per l\'aggiunta della ricetta',
            "def": carica_ricetta,
            "numero_scelta": "1"
        },
        {
            "nome": "cerca ricetta",
            "funzione_help": ' Per cercare una ricetta nel ricettario',
            "funzione": 'è stata scelta la funzione di ricerca ricetta',
            "def": ricerca_ricetta,  
            "numero_scelta": "2"
        },
        {
            "nome": "cerca per ingrediente",
            "funzione_help": " Per cercare ricette in base a un ingrediente ",
            "funzione": 'è stata scelta la funzione di ricerca per ingrediente',
            "def": ricerca_per_ingrediente,
            "numero_scelta": "3" 
        }
    ]



    time.sleep(0.4)


    while True:
        
        cont = 1
        for x in funzioni:
            print(cont , f"{x['nome']} ")
            cont += 1
        scelta = input("Scelta ( !help per ricevere aiuto): ").lower()
        
        if scelta == "!help":
            time.sleep(0.4)
            print("Di seguito sono elencate tutte le funzioni che possono essere svolte: \n")
            print("------------------")
            for funzione in funzioni:
                print(f" {funzione['nome']}: {funzione['funzione_help']}\n")
                print("------------------")
            continue  

        
        funzione_trovata = False
        for i in funzioni:
            if scelta == i["nome"] or scelta == i["numero_scelta"]:
                print(i["funzione"])
                i['def']()  
                funzione_trovata = True
                break  
            
        if not funzione_trovata:
            print("Opzione non valida. Digita '!help' per vedere le opzioni disponibili.")