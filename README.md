# Estudo de Pytest

Este repositório é dedicado ao estudo e prática de testes automatizados em Python com o framework `pytest`. Aqui, você encontra exemplos simples e práticos para aprender a escrever testes unitários.

> **Nota**: Este é um projeto educacional para prática e aprendizado. Os exemplos são simplificados para facilitar a compreensão.

## Pré-requisitos

- **Python** 3.8 ou superior ([baixe aqui](https://www.python.org/downloads/)).
- Instale o `pytest` com:
```python
pip install pytest
```

## Como usar
1. Verifique se o Python está instalado: Confirme que o Python 3.8 ou superior está instalado. No terminal, execute
```python
python --version
```
Se não estiver instalado, baixe e instale a partir de [python.org](https://www.python.org/downloads/).

2. Clone o repositório: Baixe o código do repositório e navegue até a pasta
```python
git clone https://github.com/GiovaniOrtegaFatec/Estudo_pytest.git
cd Estudo_pytest
```
3. Crie um ambiente virtual (recomendado): Para isolar as dependências do projeto, crie e ative um ambiente virtual
```python
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```
4. Instale as dependências: Instale o pytest no ambiente virtual ou globalmente
```python
pip install pytest
```
5. Verifique a instalação do pytest: Confirme que o pytest foi instalado corretamente
```python
pytest --version
```
6. Execute os testes: Rode todos os testes do repositório
```python
python -m pytest
```
Para ver detalhes dos testes executados:
```python
python -m pytest -v
```
7. Desative o ambiente virtual (se criado): Quando terminar, saia do ambiente virtual
```python
deactivate
```
## Exemplo de teste
Um exemplo de teste incluído no repositório:
```python
# test_pytest.py
def test_quando_brincadeira_receber_1_entao_deve_retornar_1():
    assert brincadeira(1) == 1
```
Para rodar este e outros testes:
```python
python -m pytest test_pytest.py
```

## Como contribuir
Quer ajudar a melhorar este repositório? Contribuições são bem-vindas! Siga estes passos:
1. Faça um fork do repositório.
2. Crie uma branch para sua alteração:
```python
git checkout -b minha-alteracao
```
3. Commit suas mudanças:
```python
git add .
git commit -m "Adiciona nova funcionalidade"
```
4. Envie para o repositório remoto:
```python
git push origin minha-alteracao
```
5. Abra um Pull Request no GitHub.

## Recursos úteis
- [Documentação do pytest](https://docs.pytest.org/)
- [Tutorial de pytest](https://realpython.com/python-testing/)

