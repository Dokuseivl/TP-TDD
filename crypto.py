import string
caracteres = string.ascii_letters + string.punctuation + string.digits + " "

def crypt(message):
    """
    Décale chaque caractère d'une position dans la table 'caracteres'.
    """
    result = ""
    for c in message:
        if c in caracteres:
            index = caracteres.index(c)
            result += caracteres[(index + 1) % len(caracteres)]
        else:
            result += c
    return result
