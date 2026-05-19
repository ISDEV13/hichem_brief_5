import pytest
from modules.calcul import carre


# --- Tests unitaires : on teste la fonction carre() directement, sans HTTP ---

def test_carre_entier_positif():
    assert carre(5) == 25

def test_carre_entier_negatif():
    assert carre(-3) == 9

def test_carre_zero():
    assert carre(0) == 0

def test_carre_flottant():
    assert carre(2.5) == 6.25

def test_carre_grand_nombre():
    assert carre(1000) == 1_000_000
