# Erstellen Sie eine Funktion, die die Summe aller ganzen Zahlen von 1 bis
# zu einem gegebenen Endwert zurückgibt.

# Lösung als Schleife:
def sum(end):
    i = 1
    sum = 0

    while i <= end:
        sum = sum + i
        i = i + 1
    
    return sum

def sum_gauss(end):
    return (end * (end + 1)) // 2