def javanais(chaine):
    # On passe la chaine en majuscule
    message = chaine.upper()
    # Initialisation de la chaine "résultat"
    resultat = ""
    # Chaines contenant la liste des consonnes et la liste des voyelles
    consonnes = "BCDFGHJKLMNPQRSTVWXZ"
    voyelles = "AEIOUY"
    # On parcourt le message à coder
    for i in range(len(message)):
        # On place le caractère lu dans la chaîne "résultat"
        resultat = resultat + message[i]
        # le "-1" permet de ne pas faire le test suivant quand on est au
        # dernier caractère
        if i < len(message) - 1:
            # Si le caractère lu est une consonne, et si le caractère suivant
            # est une voyelle...
            if message[i] in consonnes and message[i+1] in voyelles:
                # on ajoute "AV" à la chaine "résultat"
                resultat = resultat + "AV"
    return resultat

def morse(chaine):
    # On passe la chaine en majuscule
    message = chaine.upper()
    # Initialisation de la chaine "résultat"
    resultat = ""
    # Dictionnaire contenant le code morse
    code_morse = { "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", \
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", \
    "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-",  \
    "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--",    \
    "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3":   \
    "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8":     \
    "---..", "9": "----.", "0": "-----" }
    # On parcourt le message à coder
    for i in range(len(message)):
        # Si le caractère lu fait partie des caractères dans "code_morse"...
        if message[i] in code_morse:
            # ... on place sa traduction en morse dans la chaine "résultat",
            # suivie du séparateur "/"
            resultat = resultat + code_morse[message[i]] + "/"
        else:
            # sinon si le caractère lu est un espace, on ajoute juste le
            # séparateur "/" dans la chaine "résultat"
            if message[i] == " ":
                resultat = resultat + "/"
            else:
                # sinon on ajoute ? dans la chaine "résultat"
                resultat = resultat + "?/"
    # On supprime le dernier caractère de la chaine "résultat" de façon à se
    # débarasser du dernier séparateur "/" inutile
    resultat = resultat[:len(resultat)-1]
    return resultat

def decode_morse(chaine):
    # On rajoute un séparateur "/" à la fin du message à décoder
    message = chaine + "/"
    # Initialisation de la chaine "résultat"
    resultat = ""
    # Dictionnaire contenant le code morse
    code_morse = { "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", \
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", \
    "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-",  \
    "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--",    \
    "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3":   \
    "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8":     \
    "---..", "9": "----.", "0": "-----" }
    # On parcourt le message à coder pour chercher les différents motifs séparés
    # par des caractères "/". Pour cela on se sert de deux indices, debut_motif
    # qui pointe vers le premier caractère du motif, et fin_motif qui pointe
    # vers le dernier caractère du motif. Au début de la recherche, ces deux
    # indices sont initialisés à 0
    debut_motif = 0
    fin_motif = 0
    # tant que debut_motif n'a pas atteint la fin du message à décoder...
    while debut_motif < (len(message) - 1):
        # on initialise la variable "motif"...
        motif = ""
        # et on augmente fin_motif jusqu'à ce que celui-ci pointe vers un
        # caractère séparateur "/"
        while (message[fin_motif]) != "/":
            fin_motif += 1
        # Dès que fin_motif pointe vers un caractère "/", on place dans la
        # variable "motif" les caractères de "message" compris entre les
        # deux indices, debut_motif et fin_motif.
        motif = message[debut_motif:fin_motif]
        # On augmente fin_motif de 1 afin de sauter le caractère séparateur "/"
        fin_motif += 1
        # On cherche si le motif trouvé est correct, càd s'il correspond à la
        # valeur de l'une des clefs du dictionnaire contenant le code morse
        motif_correct = False
        caractere = ""
        for elt in code_morse:
            if code_morse[elt] == motif:
                motif_correct = True
                caractere = elt
        # Si le motif est dans le dictionnaire...
        if motif_correct:
            # ... on ajoute à la chaine "resultat" la clef correspondante
            resultat = resultat + caractere
        # Si le motif est vide, c'est qu'il y avait deux séparateurs "/" qui se
        # suivaient. On ajoute alors un espace à la chaine "resultat"
        elif motif == "":
            resultat = resultat + " "
        else:
            # sinon on ajoute ? dans la chaine "résultat"
            resultat = resultat + "?"
        # on initialise debut_motif et fin_motif afin de chercher le motif
        # suivant dans le message
        debut_motif = fin_motif
    return resultat