# Chiffre de César

def chiffre(chaine, decalage):
    resultat = ""
    for i in range(len(chaine)):
        car = chaine[i]
        if car >= "A" and car <= "Z":
            car = chr(ord(car) + decalage)
            if car > "Z":
                car = chr(ord(car) - 26)
            if car < "A":
                car = chr(ord(car) + 26)
        if car >= "a" and car <= "z":
            car = chr(ord(car) + decalage)
            if car > "z":
                car = chr(ord(car) - 26)
            if car < "a":
                car = chr(ord(car) + 26)
        resultat = resultat + car
    return resultat

def dechiffre(chaine, decalage):
    resultat = chiffre(chaine, -decalage)
    return resultat

def chiffre2(chaine, decalage):
    resultat = ""
    for i in range(len(chaine)):
        car = chr(ord(chaine[i])+decalage)
        resultat = resultat + car
    return resultat

def craque(message):
    for i in range(1,26):
        print(dechiffre(message,i))
    return None
