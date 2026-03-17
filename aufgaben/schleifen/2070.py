# Erstellen Sie ein Programm, welches den Durchschnitt einer endlichen Zahlenfolge
# ausgibt. Es ist ein Start- und Endwert, sowie ein Delta
# (der Wert, um die die Zahl sich vergrößert) gegeben.

start = 0
end = 5
delta = 2

summ = 0
count = 0
i = start

while i <= end:
    summ = summ + i
    i = i + delta
    count = count + 1

print(summ / count)