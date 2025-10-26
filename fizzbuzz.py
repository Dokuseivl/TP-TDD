def affiche():
    """
    Affiche les nombres de 1 à 100 en remplaçant :
    - les multiples de 3 par 'Fizz'
    - les multiples de 5 par 'Buzz'
    - les multiples de 15 par 'FrisBee'
    """
    result = ""
    for i in range(1, 101):
        if i % 15 == 0:
            result += "FrisBee"
        elif i % 3 == 0:
            result += "Fizz"
        elif i % 5 == 0:
            result += "Buzz"
        else:
            result += str(i)
    return result
