def crypt(message, pas=1):
    """
    Décale chaque caractère de 'pas' positions et ajoute le pas à la fin du message.
    """
    result = ""
    for c in message:
        if c in caracteres:
            index = caracteres.index(c)
            result += caracteres[(index + pas) % len(caracteres)]
        else:
            result += c
    result += str(pas)
    return result
