# Exercice 1 :

def trouve(chaine, caractere):
    for i in range(len(chaine)):
        if (chaine[i] == caractere):
            return True
    return False


# Exercice 2 :

def compte(chaine,caractere):
    nombre=0
    for i in range(len(chaine)):
         if (chaine[i] == caractere):
            nombre = nombre + 1
    return nombre


# Exercice 3 :

def entierNaturel(nombre):
    liste = []
    for i in range(nombre + 1):
        liste.append(i)
    return liste


# Exercice 4 :

def moyenne(liste):
    resultat = 0
    for i in range(len(liste)):
        resultat = resultat + liste[i]
    resultat = resultat / len(liste)
    return resultat


# Exercice 5 :

def noteSup10(liste):
    resultat = 0
    for i in range(len(liste)):
        if liste[i] >= 10:
            resultat = resultat + 1
    return resultat


# Exercice 6 :

def listeEnvers(liste):
    for i in range(len(liste) - 2, -1, -1):
        element = liste.pop(i)
        liste.append(element)
    return liste


# Exercice 7 :

# Version « feignants » :

def rechercheMot(mot, texte):
    if mot in texte:
        return True
    else:
        return False

# Deuxième version, plus intéressante pour la suite :

def rechercheMot(mot, texte):
    for i in range(len(texte) - len(mot) + 1):
        if texte[i:i + (len(mot))] == mot:
            return True
    return False


# Exercice 8 :

def rechercheMot(mot, texte):
    nombre = 0
    for i in range(len(texte) - len(mot) + 1):
        if texte[i:i + (len(mot))] == mot:
            nombre = nombre + 1
    return nombre


# Exercice 9 :

def pyramide(n):
    for i in range(n):
        print(" " * (n - 1 - i) + "*" * (2 * i + 1))
    return None

