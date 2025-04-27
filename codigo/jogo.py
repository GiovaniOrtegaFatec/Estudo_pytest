"""
O jogo funcionará da seguinte maneira:
Vamos pegar um número inteiro e:
- Quando o número for múltiplo de 3, deverá retornar "queijo"
- Quando o número for múltiplo de 5, deverá retornar "goiabada"
- Quando o número for múltiplo de 3 e 5, deverá retornar "Romeu e Julieta"
"""

def brincadeira(numero):
    if numero < 3:
        return numero
    if numero > 4:
        return 'goiabada'
    return 'queijo'