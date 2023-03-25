# Finden Sie die längste zusammenhängende Domino Teilfolge. Eine Domino Teilfolge ist definiert als x1y1, x2y2, wo y1=x2. (z.B: 89, 95, 54)
def domino (liste):
    end = liste[0] % 10
    max_links = max_rechts = akt_links = akt_rechts = 0
    for i in range (1,len(liste)):
        if liste[i] // 10 == end:
            akt_rechts = i
        else:
            if akt_rechts - akt_links >= max_rechts - max_links:
                max_rechts = akt_rechts
                max_links = akt_links
            akt_links = akt_rechts = i
        end = liste[i] % 10
    if akt_rechts - akt_links >= max_rechts - max_links:
        max_rechts = akt_rechts
        max_links = akt_links
    return liste [max_links : max_rechts + 1]

liste = [91,91, 12, 18, 21, 51, 91, 45, 54, 48, 67, 98, 34, 89, 95, 43, 68, 93,42,91]
print(domino(liste))

# Enfernen Sie die Zahlen die sich wiederholen
def entfernen (liste):
   neue_l = []
   for i in liste:
       if i not in neue_l:
           neue_l.append(i)
   return neue_l

# Schreiben Sie die Anzahl von symmetrischen Paaren (xy) und (yx).
def anzahl_sym (liste):
    nr = 0
    for i in range (len(liste)):
        umgekehrt = liste[i] % 10 * 10 + liste[i] // 10
        for j in range (i+1, len(liste)):
            if umgekehrt == liste[j] :
                nr += 1
    return nr

# Generieren Sie die größte mögliche Zahl, die aus der Konkatenation der Elemente der Liste gebildet ist
def grosste_zahl (liste):
    neue_l = liste[:]
    neue_l.sort (reverse = True)
    lange_zahl = ""
    for i in range(len(neue_l)):
        lange_zahl = lange_zahl + str(neue_l[i])
    return int (lange_zahl)

# Verschlüsseln Sie die Elemente der Liste, indem Sie das erste Element als Schlüssel benützen und die Methode selbst wählen (+, *, XOR)
def verschlusseln (liste):
    neue_l = liste[:]
    erste = neue_l[0]
    for i in range (1, len(neue_l)):
        neue_l[i] += erste
    return neue_l

# Filtern Sie die Zahlen, die eine bestimmte Beziehung zwischen Zahlen haben, die in einem String angegeben wird. (z.B: “x=y*3”, “x/y=2“, …
def filtern (liste, string):
    neue_liste = []
    string = string.replace("=","==")
    for zahl in liste:
        x = zahl//10
        y = zahl % 10
        if eval(string):
            neue_liste.append(zahl)
    return neue_liste

def grosster_gemainsemer_divisor (a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def kleinsten_gemainsamen_vielfachten (a,b):
    return a*b//grosster_gemainsemer_divisor(a,b)

# Finden Sie den kleinsten gemeinsamen Vielfachen zwischen Index from und to, welche gegeben sind
def teilfolge_kgv (liste, fromm, to):
    vielfachten = kleinsten_gemainsamen_vielfachten (liste[fromm], liste[fromm+1])
    for i in range (fromm+2, to+1):
       vielfachten = kleinsten_gemainsamen_vielfachten(vielfachten, liste[i])
    return vielfachten

# print(entfernen(liste))
# print(anzahl_sym(liste))
# print(grosste_zahl(liste))
# print(verschlusseln(liste))
# print(filtern(liste,"x/y=2"))
# print (teilfolge_kgv(liste,3,5))