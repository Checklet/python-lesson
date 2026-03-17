# Erstellen Sie ein Programm, welches für eine Zeichenkette (String) ausgibt,
# ob es ein Vokal hat – und welches Vokal – oder nicht.

text = "Julian"

if text.find("a") > -1:
    print(text + " hat ein 'A'.")

if text.find("e") > -1:
    print(text + " hat ein 'E'.")

if text.find("i") > -1:
    print(text + " hat ein 'I'.")

if text.find("o") > -1:
    print(text + " hat ein 'O'.")

if text.find("u") > -1:
    print(text + " hat ein 'U'.")
