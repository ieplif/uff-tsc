import pytest
from jogo_da_forca import Forca
    

@pytest.fixture
def jogo_forca():
    tema = "animais"
    palavra = "girafa"
    return Forca(tema, palavra)

def test_adivinhar_letra_correta(jogo_forca):
    jogo_forca.adivinhar('g')
    assert 'g' in jogo_forca.letras_corretas

def test_adivinhar_letra_errada(jogo_forca):
    jogo_forca.adivinhar('x')
    assert 'x' in jogo_forca.letras_erradas

def test_ganhou(jogo_forca):
    jogo_forca.adivinhar('g')
    jogo_forca.adivinhar('i')
    jogo_forca.adivinhar('r')
    jogo_forca.adivinhar('a')
    jogo_forca.adivinhar('f')
    assert jogo_forca.ganhou() == True

def test_perdeu(jogo_forca):
    jogo_forca.adivinhar('x')
    jogo_forca.adivinhar('y')
    jogo_forca.adivinhar('z')
    jogo_forca.adivinhar('w')
    jogo_forca.adivinhar('v')
    jogo_forca.adivinhar('u')
    assert jogo_forca.perdeu() == True

def test_palavra_escondida(jogo_forca):
    assert jogo_forca.palavra_escondida() == "______"

def test_palavra_escondida_com_letra_advinhada(jogo_forca):
    jogo_forca.adivinhar('g')
    assert jogo_forca.palavra_escondida() == "g_____"
