markdown

Copiar
# Estudo de Pytest

Bem-vindo ao repositório **Estudo de Pytest**! Este projeto é dedicado ao aprendizado e prática de testes automatizados em Python usando o framework `pytest`. Aqui, você encontrará exemplos práticos, exercícios e dicas para escrever testes eficientes e robustos.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/pytest-7.0+-green.svg)](https://docs.pytest.org/)

## 🎯 Objetivo

O objetivo deste repositório é servir como um guia prático para iniciantes e desenvolvedores intermediários que desejam aprender a criar testes automatizados com `pytest`. Ele inclui exemplos de testes unitários, testes de integração e boas práticas para organização de código.

## 📋 Pré-requisitos

- **Python** 3.8 ou superior instalado ([baixe aqui](https://www.python.org/downloads/)).
- **pytest** instalado. Para instalar, execute:

  ```bash
  pip install pytest
🚀 Como usar
Clone o repositório:

bash

Copiar
git clone https://github.com/GiovaniOrtegaFatec/Estudo_pytest.git
cd Estudo_pytest
Instale as dependências:

bash

Copiar
pip install -r requirements.txt
Execute os testes:

bash

Copiar
pytest
Para ver detalhes dos testes, use:

bash

Copiar
pytest -v
📂 Estrutura do repositório
text

Copiar
Estudo_pytest/
├── tests/                # Pasta com os arquivos de teste
│   ├── test_exemplo1.py  # Exemplo de teste unitário
│   ├── test_exemplo2.py  # Exemplo de teste de integração
├── src/                  # Código-fonte das funções testadas
│   ├── calculadora.py    # Exemplo de módulo com funções
├── requirements.txt      # Dependências do projeto
└── README.md             # Este arquivo
🧪 Exemplos de testes
Aqui está um exemplo de teste incluído no repositório:

python

Copiar
# tests/test_exemplo1.py
def test_soma():
    assert 1 + 1 == 2
Para rodar apenas este teste:

bash

Copiar
pytest tests/test_exemplo1.py
🤝 Como contribuir
Contribuições são bem-vindas! Siga os passos abaixo:

Faça um fork do repositório.
Crie uma branch para sua feature:
bash

Copiar
git checkout -b minha-feature
Commit suas alterações:
bash

Copiar
git commit -m "Adiciona nova feature"
Envie para o repositório remoto:
bash

Copiar
git push origin minha-feature
Abra um Pull Request.
Por favor, leia o  para mais detalhes.

📚 Recursos adicionais
Documentação oficial do pytest
Tutorial de pytest para iniciantes
Boas práticas de testes automatizados
📬 Contato
Se tiver dúvidas ou sugestões, entre em contato:

Autor: Giovani Ortega
Email: giovani.ortega@example.com
GitHub: GiovaniOrtegaFatec
