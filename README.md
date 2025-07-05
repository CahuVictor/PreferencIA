# PreferencIA

[![Python](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**PreferencIA** é um sistema de recomendação que transforma tabelas de avaliações  
(`user_id`, `item_id`, `rating`) em listas de itens sugeridos, usando **filtragem
colaborativa** com **SVD** (biblioteca [Surprise]).  

> Projeto desenvolvido originalmente como parte da disciplina **Sistemas de
> Recomendação** do MBA em Data Science & Analytics (Senac), ministrada pelo
> professor **Alex Cunha**.

---

## 📌 Sumário

- [📚 Sistema de Recomendação de Livros com SVD](#-sistema-de-recomendação-de-livros-com-svd)
  - [📌 Sumário](#-sumário)
  - [📚 Sobre o Projeto](#-sobre-o-projeto)
  - [🚀 Objetivo](#-objetivo)
  - [🛠️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
  - [📂 Estrutura do Projeto](#-estrutura-do-projeto)
  - [🐍 Ambiente Python com Poetry](#-ambiente-python-com-poetry)
  - [▶️ Execução do Projeto](#️-execução-do-projeto)
  - [📄 Documentação Adicional](#-documentação-adicional)

---

## 📚 Sobre o Projeto

Este sistema de recomendação oferece sugestões personalizadas de livros para usuários com base nas avaliações de outros usuários com gostos semelhantes. Ele utiliza o algoritmo **Singular Value Decomposition (SVD)** da biblioteca `scikit-surprise`.

---

## 🚀 Objetivo

- Construir um modelo de recomendação utilizando SVD.
- Avaliar a performance do modelo com métricas como RMSE.
- Gerar recomendações personalizadas para qualquer usuário ativo.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11**
- **Poetry** para gerenciamento de dependências e ambiente virtual
- **Pandas** para manipulação de dados
- **NumPy / SciPy** para computação científica
- **scikit-learn** 
- [Surprise](http://surpriselib.com)   

---

## 📂 Estrutura do Projeto

```
pos/
├── docs
│   ├── AMBIENTE_POETRY.md              # Guia completo de instalação do ambiente virtual
│   ├── CONFIGURAR_VSCODE_POWERSHELL.md # Como configurar o terminal do VS Code
│   └── EXPLICACAO_PROJETO.md           # Explicação detalhada do funcionamento do projeto e código
├── src
│   ├── __init__.py
│   ├── dados.py                        # Carregamento e pré-processamento de dados
│   ├── modelo.py                       # Treinamento e avaliação do modelo SVD
│   ├── recomendador.py                 # Função de recomendação de livros
│   └── main.py                         # Script principal para execução via terminal
├── tests
│   └── __init__.py
├── pyproject.toml                      # Arquivo de configuração do Poetry com as dependências
├── poetry.lock                         # Lockfile gerado automaticamente com versões exatas
└── README.md                           # Este arquivo
```

---

## 🐍 Ambiente Python com Poetry

O projeto utiliza o Poetry. Para instruções completas de instalação e ativação do ambiente, consulte o arquivo [`AMBIENTE_POETRY.md`](./docs/AMBIENTE_POETRY.md).

---

## ▶️ Execução do Projeto

Ative o ambiente virtual via `poetry shell`.

No main.py, selecione qual projeto será usado, alterando a variável project_number para 1, para rodar com os dados antigos e para 2 para rodar com os novos dados do kagle. Os dados do kagle devem estar na pasta data com os nomes originais.

```bash
python src/pos/main.py --user_id 1 --top_n 5
```

Você verá na tela uma lista de livros recomendados para o usuário especificado, além da criação de um arquivo `.csv` com as recomendações.

---

## 📄 Documentação Adicional

* [Explicação detalhada do projeto e do código](./docs/EXPLICACAO_PROJETO.md)
* [Como configurar o VS Code para usar PowerShell](./docs/CONFIGURAR_VSCODE_POWERSHELL.md)

---

Mantenha seu ambiente sempre sincronizado com `poetry install` caso novas dependências sejam adicionadas.
