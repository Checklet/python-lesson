# Erstellen Sie ein Programm, das für jede Zahl von 1 bis 100 ausgibt, durch
# welche Zahlen sie teilbar ist.

i = 4

while i <= 100:
    if i % 2 == 0:
        print(str(i) + " ist durch 2 teilbar.")
    
    if i % 3 == 0:
        print(str(i) + " ist durch 3 teilbar.")

    if i % 5 == 0:
        print(str(i) + " ist durch 5 teilbar.")

    if i % 7 == 0:
        print(str(i) + " ist durch 7 teilbar.")

    i = i + 1
