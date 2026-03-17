# Erstellen Sie ein Programm, welches die Fakultät einer Zahl ausgibt.

n = 6

i = 1
f = 1

while i <= n:
    f = f * i
    i = i + 1

print(str(n) + "! = " + str(f))