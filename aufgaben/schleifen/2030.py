# Erstellen Sie ein Programm, welches das kleine 1-mal-1 ausgibt.

a = 1
b = 1

while a <= 10:
    while b <= 10:
        print(str(a) + " * " + str(b) + " = " + str(a * b))
        b = b + 1
    b = 1
    a = a + 1
