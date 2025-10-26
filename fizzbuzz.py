def affiche(n1=1, n2=100):
    """
    Version finale : affiche les nombres de n1 à n2 inclus.
    """
    result = ""
    for i in range(n1, n2 + 1):
        if i % 15 == 0:
            result += "FrisBee"
        elif i % 3 == 0:
            result += "Fizz"
        elif i % 5 == 0:
            result += "Buzz"
        else:
            result += str(i)
    return result
