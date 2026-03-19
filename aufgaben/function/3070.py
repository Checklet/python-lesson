# Erstellen Sie eine Funktion, die das Ergebnis der Funktion f(x) = 2.5x - 9 zurückgibt.
# Das Programm soll für den Definitionsbereich -10 bis 10 in Abständen von 0.25 den Wert 
# zurückgeben.

def f(x):
    return 2.5 * x - 9

i = -10.0

while i <= 10.0:
    print("f(" + str(i) + ") = " + str(f(i)))
    i = i + 0.25