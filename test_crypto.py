import pytest
from crypto import crypt
from crypto import decrypt

def test_crypt_simple():
    """Teste le cryptage simple (+1 ASCII)."""
    assert crypt("abc") == "bcd"

def test_crypt_avec_pas():
    """Teste le cryptage avec pas variable."""
    result = crypt("abc", 2)
    assert result.startswith("cde")
    assert result.endswith("2")
    
def test_decrypt_message():
    """Teste le décryptage d’un message."""
    msg = crypt("Hello!", 3)
    assert decrypt(msg) == "Hello!"
