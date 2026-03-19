# Erstellen Sie eine Funktion, die eine statische Fehlermeldung ausgibt,
# wenn sie aufgerufen wird. Das Programm soll die Funktion aufrufen, wenn 
# der Betrag einer Zahl größer oder gleich 1024 ist.

def alert():
    print("Alarm")

i = 1067

if i >= 1024:
    alert()