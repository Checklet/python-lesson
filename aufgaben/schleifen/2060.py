# Erstellen Sie ein Programm, welches das Collatz-Problem wiedergibt:
# Es ist eine ganze Zahl gegeben.
# Wenn die Zahl ungerade ist, soll diese mit 3 multipliziert und mit 1 addiert werden.
# Sobald die Zahl gerade ist, soll diese durch zwei geteilt werden.
# Dieser Prozess soll solange durchgeführt werden, bis die Zahl 1 ist oder
# bis 25 Durchläufe gemacht wurden.
# Nach jedem Prozess soll die aktuelle Zahl ausgegeben werden.

n = 39
print(n)

i = 0

while i <= 25 and n != 1:
    while n % 2 == 1:
        n = 3 * n + 1

    while n % 2 == 0:
        n = n // 2

    print(n)
    i = i + 1