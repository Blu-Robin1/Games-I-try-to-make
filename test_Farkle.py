from Farkle import Die
import pytest

def test_die():
    x=Die()
    assert x.value in list(range(0,7))
