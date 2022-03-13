# Wir bauen eine Software für einen Bankautomaten
## Wir brauchen ein Benutzerkonto
    # Bei erstmaliger Benutzung wird der Kunde dazu aufgefordet eins anzulegen
    # Dieses besteht aus Name, Kontonummer und zugehöriger Geheimzahl
    # Nach erfolgreicher Eingabe kann ebenfalls der aktuelle Kontostand eingesehen werden
## Danach definieren wir die verschiedenen Funkitionen
    # Einzahlen, Auszahlen, Kontostand und Beenden
    # Die Verschiedenen Möglichkeiten wollen wir in Funktionen unterteilen
## Bei fehlerhafter Eingabe sollen verschiedene Fehlermeldungen angezeigt werden

def check_account_number ():
    """Eine Funktion, die Prüft, ob das Format der angegeben Kontonummer passt.

    Args: len(kontonummer) > or < 10

    Returns: kontonummer
    """
    print("Geben Sie Nun Ihre Kontonummer ein: ")
    kontonummer = input() 

    while kontonummer:  
        
        if len(kontonummer) > 10 or len(kontonummer)< 10:
            kontonummer == False   
            kontonummer = input("\nBitte geben Sie die Kontonummer nochmal ein: \n")  
            continue
        else:
            kontonummer == True
            print("\nDie angegebene Kontonummer passt.")
        break

    return kontonummer

print("Hallo! Bitte geben Sie ihren Namen ein: ")
name = input()

print("Ihr Konto wird unter dem Namen " + name + " angelegt.")

check_account_number()

print





