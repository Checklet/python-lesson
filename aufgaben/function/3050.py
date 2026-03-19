# Erstellen Sie eine Funktion, die eine Zahl annimmt. Ist diese Zahl gerade, soll
# sie halbiert werden. Ansonsten soll sie verdreifacht und um 1 addiert werden.
# In beiden Fällen soll die Zahl ausgegeben werden.

def collatz_step(n):
    if n % 2 == 0:
        print(n // 2)

    else:
        print(3 * n + 1)
