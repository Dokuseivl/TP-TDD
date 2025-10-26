def decrypt(message):
    """
    Déchiffre le message crypté en utilisant le pas à la fin de la chaîne.
    """
    pas = int(message[-1])
    message = message[:-1]
    result = ""
    for c in message:
        if c in caracteres:
            index = caracteres.index(c)
            result += caracteres[(index - pas) % len(caracteres)]
        else:
            result += c
    return result

