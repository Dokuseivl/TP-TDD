import pytest
from fizzbuzz import affiche

def test_affiche_sans_parametre():
    """
    Vérifie que la fonction affiche() renvoie bien une chaîne contenant
    Fizz, Buzz, et FrisBee sur les nombres de 1 à 100.
    """
    result = affiche()
    assert "Fizz" in result
    assert "Buzz" in result
    assert "FrisBee" in result
    assert result.startswith("12Fizz")

def test_affiche_avec_parametre():
    """Teste la version avec un paramètre n."""
    result = affiche(15)
    assert result == "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee"

def test_affiche_deux_parametres():
    """Teste l'affichage entre deux bornes."""
    assert affiche(5, 10) == "BuzzFizz78FizzBuzz"
    assert affiche(10, 16) == "Buzz11Fizz1314FrisBee16"
