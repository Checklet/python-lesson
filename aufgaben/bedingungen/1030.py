# Erstellen Sie ein Programm, das für eine Zeichenkette (String) ausgibt,
# ob es den Buchstaben 'N' findet, und wo. Nur Großbuchstaben werden betrachtet.

text = "JULIAN"

position_of_n = text.find("N")

if position_of_n < 0:
    print("Es gibt kein 'N' in " + text)
else:
    print("Das 'N' in " + text + " ist am " + str(position_of_n + 1) + ". Platz.")