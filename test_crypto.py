import pytest
from src.crypto import crypt

def test_crypt_simple():
    """Teste le cryptage simple (+1 ASCII)."""
    assert crypt("abc") == "bcd"
