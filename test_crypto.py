import pytest
from crypto import crypt

def test_crypt_simple():
    """Teste le cryptage simple (+1 ASCII)."""
    assert crypt("abc") == "bcd"

def test_crypt_avec_pas():
    """Teste le cryptage avec pas variable."""
    result = crypt("abc", 2)
    assert result.startswith("cde")
    assert result.endswith("2")
    
