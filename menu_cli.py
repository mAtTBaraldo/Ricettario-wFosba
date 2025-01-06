import time, os, random
from carica_ricetta import carica_ricetta
from cerca_ricetta import ricerca_ricetta
from cerca_ingrediente import ricerca_per_ingrediente
from ricerca_per_ingredienti import ricerca_per_ingredienti
from elimina_ricetta import elimina_ricetta
from modifica_ricetta import modifica_ricetta
from mostra_ricette import mostra_ricette
from colorama import Fore

# Dizionario delle traduzioni
translations = {
    'en': {
        'choose_language': "Choose your language (en/it): ",
        'invalid_option': "Invalid option. Type '!help' to see available options.",
        'input_prompt': "Choice (type !help for assistance): ",
        'menu_header': "Please choose an option:",
        'help_header': "The following functions can be performed: ",
        'separator': "------------------",
    },
    'it': {
        'choose_language': "Scegli la tua lingua (en/it): ",
        'invalid_option': "Opzione non valida. Digita '!help' per vedere le opzioni disponibili.",
        'input_prompt': "Scelta (scrivi !help per ricevere aiuto): ",
        'menu_header': "Si prega di scegliere un'opzione:",
        'help_header': "Di seguito sono elencate tutte le funzioni che possono essere svolte: ",
        'separator': "------------------",
    }
}

ascii_art = r"""
   ___  ____________________________   ___  ________ 
  / _ \/  _/ ___/ __/_  __/_  __/ _ | / _ \/  _/ __ \
 / , _// // /__/ _/  / /   / / / __ |/ , _// // /_/ /
/_/|_/___/\___/___/ /_/   /_/ /_/ |_/_/|_/___/\____/ 
                                                     
"""
lista_colori = [
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.CYAN,
    Fore.WHITE
]

def choose_language():
    while True:
        lang = input(translations['en']['choose_language']).lower()
        if lang in translations:
            os.system('cls')
            return lang

        else:
            print("Language not supported. Try again.")
            os.system('cls')

def menu():
    lang = choose_language()
    funzioni = [
    {
        "nome": {
            "it": "aggiungi ricetta",
            "en": "add recipe"
        },
        "funzione_help": {
            "it": " Per aggiungere una nuova ricetta al ricettario",
            "en": " To add a new recipe to the cookbook"
        },
        "funzione": {
            "it": "è stata scelta la funzione per l'aggiunta della ricetta",
            "en": "the function to add the recipe has been selected"
        },
        "def": carica_ricetta,
        "numero_scelta": "1"
    },
    {
        "nome": {
            "it": "cerca ricetta",
            "en": "search recipe"
        },
        "funzione_help": {
            "it": " Per cercare una ricetta nel ricettario",
            "en": " To search for a recipe in the cookbook"
        },
        "funzione": {
            "it": "è stata scelta la funzione di ricerca ricetta",
            "en": "the recipe search function has been selected"
        },
        "def": ricerca_ricetta,
        "numero_scelta": "2"
    },
    {
        "nome": {
            "it": "cerca per ingrediente",
            "en": "search by ingredient"
        },
        "funzione_help": {
            "it": " Per cercare ricette in base a un ingrediente",
            "en": " To search for recipes based on an ingredient"
        },
        "funzione": {
            "it": "è stata scelta la funzione di ricerca per ingrediente",
            "en": "the function to search by ingredient has been selected"
        },
        "def": ricerca_per_ingrediente,
        "numero_scelta": "3"
    },
    {
        "nome": {
            "it": "cerca per ingredienti",
            "en": "search by ingredients"
        },
        "funzione_help": {
            "it": " Per cercare ricette in base a molteplici ingredienti",
            "en": " To search for recipes based on multiple ingredients"
        },
        "funzione": {
            "it": "è stata scelta la funzione di ricerca per ingredienti",
            "en": "the function to search by ingredients has been selected"
        },
        "def": ricerca_per_ingredienti,
        "numero_scelta": "4"
    },
    {
        "nome": {
            "it": "modifica ricetta",
            "en": "modify recipe"
        },
        "funzione_help": {
            "it": " Per modificare una ricetta",
            "en": " To modify a recipe"
        },
        "funzione": {
            "it": "è stata scelta la funzione per modificare una ricetta",
            "en": "the function to modify a recipe has been selected"
        },
        "def": modifica_ricetta,
        "numero_scelta": "5"
    },
    {
        "nome": {
            "it": "mostra ricette",
            "en": "show recipes"
        },
        "funzione_help": {
            "it": " Per mostrare tutte le ricette",
            "en": " To show all the recipes"
        },
        "funzione": {
            "it": "è stata scelta la funzione per mostrare tutte le ricette",
            "en": "the function to show all the recipes has been selected"
        },
        "def": mostra_ricette,
        "numero_scelta": "6"
    },
    {
        "nome": {
            "it": "elimina ricetta",
            "en": "delete recipe"
        },
        "funzione_help": {
            "it": " Per eliminare una ricetta",
            "en": " To delete a recipe"
        },
        "funzione": {
            "it": "è stata scelta la funzione per eliminare una ricetta",
            "en": "the function to delete a recipe has been selected"
        },
        "def": elimina_ricetta,
        "numero_scelta": "7"
    }
]
    time.sleep(0.4)
    while True: 
        color = random.choice(lista_colori)
        print(color + ascii_art + Fore.WHITE)
        print(translations[lang]['menu_header'])
        cont = 1
        for x in funzioni:
            print(f"{cont}. {x['nome'][lang]}")  # Modificato per stampare solo il nome della funzione
            cont += 1
            
        scelta = input(translations[lang]['input_prompt']).strip().lower()

        if scelta == "!help":
            time.sleep(0.4)
            print("\n",translations[lang]['help_header'])
            print(translations[lang]['separator'])
            for funzione in funzioni:
                print(f" {funzione['nome'][lang]}: {funzione['funzione_help'][lang]}\n")
                print(translations[lang]['separator'])
            continue  

        funzione_trovata = False
        os.system('cls')
        for i in funzioni:
            if scelta == i["nome"][lang] or scelta == i["numero_scelta"]:
                print(i["funzione"][lang])  # Modificato per stampare la descrizione della funzione
                i['def'](lang)  
                funzione_trovata = True
                break  
            
        if not funzione_trovata:
            print(translations[lang]['invalid_option'])
