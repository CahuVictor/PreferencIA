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

- [📚 Sobre o Projeto](#-sobre-o-projeto)
- [🚀 Objetivo](#-objetivo)
- [🛠️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
- [📂 Estrutura do Projeto](#-estrutura-do-projeto)
- [🐍 Ambiente Python com Poetry](#-ambiente-python-com-poetry)
- [▶️ Execução do Projeto](#️-execução-do-projeto)
- [🧩 Documentação Adicional](#-documentação-adicional)

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
│   └── recomendador.py                 # Script principal com o modelo SVD e recomendações
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

Com o ambiente ativado via `poetry shell`, rode o script principal:

```bash
python recomendador.py
```

Você verá na tela uma lista de livros recomendados para o usuário especificado.

---

## 🧩 Documentação Adicional

- 📘 [Explicação detalhada do projeto e do código](./docs/EXPLICACAO_PROJETO.md)
- 🖥️ [Como configurar o VS Code para usar PowerShell](./docs/CONFIGURAR_VSCODE_POWERSHELL.md)

---

Mantenha seu ambiente sempre sincronizado com `poetry install` caso novas dependências sejam adicionadas.