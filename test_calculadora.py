import pytest
from calculadora import somar, subtrair, multiplicar, dividir


def test_somar():
    assert somar(2, 3) == 99 #valor errado intencionalmente
    assert somar(-1, 1) == 0


def test_subtrair():
    assert subtrair(5, 3) == 2


def test_multiplicar():
    assert multiplicar(3, 4) == 12


def test_dividir():
    assert dividir(10, 2) == 5.0


def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(5, 0)