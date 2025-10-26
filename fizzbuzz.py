def affiche(n=100):
    """
    Même principe que précédemment, mais jusqu’à n.
    """
    result = ""
    for i in range(1, n + 1):
        if i % 15 == 0:
            result += "FrisBee"
        elif i % 3 == 0:
            result += "Fizz"
        elif i % 5 == 0:
            result += "Buzz"
        else:
            result += str(i)
    return result
