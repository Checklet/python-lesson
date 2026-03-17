# Erstellen Sie ein Programm, welches stufenförmig Zeichenketten ausgibt für eine
# Zahl n.
# 
# Beispiel: (n = 5)
# 
# *
# **
# ***
# ****
# ***** 

n = 5
i = 0
j = 0

step = ""

while i < n:
    while j <= i:
        step = step + "*"
        j = j + 1
    print(step)
    step = ""
    j = 0
    i = i + 1