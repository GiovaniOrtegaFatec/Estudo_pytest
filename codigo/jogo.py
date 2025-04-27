"""
Jogo que retorna uma string com base em divisibilidade:
- Múltiplo de 3 e 5: 'Romeu e Julieta'
- Múltiplo de 3: 'queijo'
- Múltiplo de 5: 'goiabada'
- Caso contrário: o próprio número
Parâmetro:
    numero (int): Número inteiro a ser avaliado
Retorno:
    str ou int: String correspondente ou o número de entrada
"""

def brincadeira(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return 'Romeu e Julieta'
    elif numero % 3 == 0:
        return 'queijo'
    elif numero % 5 == 0:
        return 'goiabada'
    return numero