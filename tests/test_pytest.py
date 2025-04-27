from pytest import mark
from codigo.jogo import brincadeira

"""
O teste é formado por 3 etapas (GWT - AAA):

- Given - Dado
- When - Quando
- Then - Então
OU
- Arrange
- Act
- Assert

"""

def test_quando_brincadeira_receber_1_entao_deve_retornar_1():
    assert brincadeira(1) == 1
    
    # Versão explicada do código:

    """entrada = 1 # Dado
    esperado = 1 # Dado

    resultado = brincadeira(entrada) # Quando

    assert resultado == esperado # Então"""


def test_quando_brincadeira_receber_2_entao_deve_retornar_2():
    assert brincadeira(2) == 2


def test_quando_brincadeira_receber_3_entao_deve_retornar_queijo():
    assert brincadeira(3) == 'queijo'


@mark.goiabada
def test_quando_brincadeira_receber_5_entao_deve_retornar_goiabada():
    assert brincadeira(5) == 'goiabada'

@mark.goiabada
def test_quando_brincadeira_receber_10_entao_deve_retornar_goiabada():
    assert brincadeira(10) == 'goiabada'

@mark.goiabada
def test_quando_brincadeira_receber_20_entao_deve_retornar_goiabada():
    assert brincadeira(20) == 'goiabada'
