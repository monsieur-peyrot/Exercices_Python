def longueclef(texte, clef):
    resultat = ''
    j = 0
    for i in range(len(texte)):
        resultat = resultat + clef[j]
        j = j + 1
        if j == len(clef):
            j = 0
    return resultat

def chiffre_vigenere(texte, clef):
    resultat = ''
    clef = longueclef(texte, clef)
    for i in range(len(texte)):
        code = ord(texte[i]) + ord(clef[i])
        resultat = resultat + chr(code)
    return resultat

def dechiffre_vigenere(texte, clef):
    resultat = ''
    clef = longueclef(texte, clef)
    for i in range(len(texte)):
        code = ord(texte[i]) - ord(clef[i])
        if code < 0:
            code = 0
        resultat = resultat + chr(code)
    return resultat

message = "Bonjour les amis !"
clef =    "ceci est une clef!"
clef2 =   "R\x93\x85~;º\x99O9º\x9305\x84\x86\x85f!"
print(message, len(message))
print(clef, len(clef))
print(clef2, len(clef2))

