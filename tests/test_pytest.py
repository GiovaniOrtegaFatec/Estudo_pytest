from pytest import mark,fixture
from codigo.jogo import brincadeira

# Pytest usa asserts simples do Python, com relatórios detalhados de falhas, facilitando a escrita e depuração de testes.

# @pytest.fixture cria funções reutilizáveis para configurar dados ou estados, correspondendo à fase 'Arrange' do modelo AAA.

# @pytest.mark.parametrize executa o mesmo teste com diferentes entradas, reduzindo duplicação e cobrindo múltiplos cenários.

# @pytest.mark permite categorizar e configurar testes (ex.: skip, xfail, personalizado). Marcadores personalizados devem ser registrados no pytest.ini.

# Pytest fornece relatórios detalhados de falhas e suporta depuração com --pdb ou análise de desempenho com --durations.

# Configurações e marcadores personalizados são definidos em pytest.ini ou pyproject.toml para centralizar e evitar warnings.

# Pytest suporta plugins (ex.: pytest-cov, pytest-xdist) para adicionar funcionalidades como cobertura de código ou testes paralelos.

# Pytest enfatiza simplicidade (asserts), reutilização (fixtures, parametrização), flexibilidade (marcadores), relatórios detalhados, e extensibilidade (plugins).

# A comunidade do Pytest é ativa, com contribuições via Open Collective, Tidelift e GitHub. Plugins como pytest-cov e pytest-xdist ampliam sua funcionalidade, e recursos educacionais (ex.: Real Python, freeCodeCamp) ajudam na adoção.

# Pytest é aplicável a testes unitários, de integração, funcionais, e especializados (ex.: web, redes, ML), com suporte a CI/CD, plugins (pytest-cov, pytest-xdist), e relatórios detalhados.

# Uma fixture é uma forma de evitar repetição de código em testes
"""
Fixture para fornecer dados de teste comuns para a função brincadeira.
Retorna uma lista de tuplas (entrada, esperado) para testar múltiplos casos.
"""
@fixture
def casos_de_teste():
    return [
        (1, 1),              # Número não múltiplo de 3 ou 5
        (2, 2),              # Número não múltiplo de 3 ou 5
        (3, 'queijo'),       # Múltiplo de 3
        (5, 'goiabada'),     # Múltiplo de 5
        (15, 'Romeu e Julieta')  # Múltiplo de 3 e 5
    ]

"""
O teste é formado por 3 etapas (GWT - AAA):

- Given - Dado
- When - Quando
- Then - Então
OU
- Arrange
- Act
- Assert

xUnit Patterns - Gerard Mezaros

- Setup - Dado
- Exercise - Quando
- Verify - Então
- TearDown - "Desmonta tudo antes que seja tarde"

"""
# Testes para números comuns
def test_quando_brincadeira_receber_1_entao_deve_retornar_1():
    assert brincadeira(1) == 1
    
    # Versão explicada do código:
    """
    entrada = 1 # Dado
    esperado = 1 # Dado
    resultado = brincadeira(entrada) # Quando
    assert resultado == esperado # Então
    """


def test_quando_brincadeira_receber_2_entao_deve_retornar_2():
    assert brincadeira(2) == 2

# Testes para múltiplos de 3 ('queijo')
def test_quando_brincadeira_receber_3_entao_deve_retornar_queijo():
    assert brincadeira(3) == 'queijo'

# @pytest.mark é um decorador do Pytest para marcar e configurar testes. 
# Ex.: xfail (falha esperada), parametrize (múltiplos dados), skip (pular teste).
# @pytest.mark.goiabada é um marcador personalizado para agrupar testes relacionados à saída 'goiabada'.
# Testes para múltiplos de 5 ('goiabada'):
@mark.goiabada
def test_quando_brincadeira_receber_5_entao_deve_retornar_goiabada():
    assert brincadeira(5) == 'goiabada'

@mark.goiabada
def test_quando_brincadeira_receber_10_entao_deve_retornar_goiabada():
    assert brincadeira(10) == 'goiabada'


# @pytest.mark.skip pula a execução de um teste. 
# Usa reason="motivo" para explicar por que o teste é ignorado.
@mark.skip(reason='ainda não implementei') #serve para pular teste que ainda não deve ser feito
def test_quando_brincadeira_receber__1_entao_deve_retornar_None():
    assert brincadeira(20) == 'goiabada'


# Testa múltiplos de 3 para garantir que a função retorna 'queijo'.
@mark.parametrize(
        'entrada',
        [3, 6, 9, 12, 18]
)
def test_brincadeira_deve_retornar_queijo_com_multiplos_de_3(entrada):
    assert brincadeira(entrada) == 'queijo'


# @pytest.mark.parametrize permite executar um teste com múltiplos conjuntos de dados.
# @mark.usa_casos_de_teste marca testes que usam a fixture 'casos_de_teste'; execute com 'pytest -m usa_casos_de_teste'.
@mark.usa_casos_de_teste
@mark.parametrize('entrada, esperado', [(1, 1), (2, 2), (3, 'queijo'), (4, 4), (5, 'goiabada')])
def test_brincadeira_deve_retornar_valor_esperado(entrada, esperado):
    assert brincadeira(entrada) == esperado

# Testes para múltiplos de 3 e 5 usando a fixture casos_de_teste
@mark.usa_casos_de_teste
def test_quando_brincadeira_receber_multiplos_3_e_5_entao_deve_retornar_romeu_e_julieta(casos_de_teste):
    for entrada, esperado in casos_de_teste: # Itera sobre cada par (entrada, esperado) da fixture 'casos_de_teste'.
        if esperado == 'Romeu e Julieta': # Verifica se o valor esperado é 'Romeu e Julieta' (múltiplo de 3 e 5).
            assert brincadeira(entrada) == esperado # Testa se brincadeira(entrada) retorna 'Romeu e Julieta' como esperado.



# @pytest.mark.xfail marca teste como esperado para falhar (bug ou funcionalidade pendente).
# Usa reason="motivo", strict, raises, run.
import sys

@mark.xfail(sys.platform == 'win32', reason="Funcionalidade não suportada no Windows")
def test_xfail_windows():
    assert brincadeira(20) != 'goiabada'

@mark.xfail(reason="Bug conhecido: comportamento incorreto para entrada 20")
def test_xfail2():
    assert brincadeira(20) == 'goiabada'

# @pytest.mark.skipif pula um teste se uma condição for verdadeira. 
# Usa reason="motivo" e uma expressão condicional (ex.: sys.version).
@mark.skipif(sys.platform == 'win32', reason="Teste pulado no Windows devido a comportamento instável")
def test_xfail_windows_skip():
    assert brincadeira(20) != 'goiabada'

# @pytest.mark.stdout é um marcador personalizado para testes que verificam a saída padrão (stdout).
# A fixture capsys captura stdout e stderr, permitindo testar impressões na tela.
@mark.stdout
def test_brincadeira_deve_escrever_entrei_na_brincadeira_na_tela(capsys):
    brincadeira(0)
    resultado = capsys.readouterr()
    assert resultado.out == 'Entrei na brincadeira!\n'