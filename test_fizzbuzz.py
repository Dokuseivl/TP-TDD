import pytest
from src.fizzbuzz import affiche

def test_affiche_sans_parametre():
    """
    V�rifie que la fonction affiche() renvoie bien une cha�ne contenant
    Fizz, Buzz, et FrisBee sur les nombres de 1 � 100.
    """
    result = affiche()
    assert "Fizz" in result
    assert "Buzz" in result
    assert "FrisBee" in result
    assert result.startswith("12Fizz")
