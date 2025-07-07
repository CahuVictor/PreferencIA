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

## ✨ Principais recursos

- **Pipeline completo**: leitura do dataset, pré-processamento, treino, avaliação
  (RMSE) e geração de top-N recomendações.
- **Modelo base SVD** facilmente trocável por outras abordagens (KNN, ALS,
  implícitos, híbridos).
- **Filtros prontos** para descartar usuários/itens com poucas avaliações.
- **Relatórios** simples em CSV para métricas e recomendações.
- **Código limpo** focado em didática, pronto para forks e experimentos.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11**
- **Poetry** para gerenciamento de dependências e ambiente virtual
- **Pandas** para manipulação de dados
- **NumPy / SciPy** para computação científica
- **scikit-learn** 
- [Surprise](http://surpriselib.com)
- (Futuro) pre-commit (lint & format)

---

## 📂 Estrutura do Projeto

```
preferencia/
├── data/            # datasets de entrada
├── outputs/         # métricas e recomendações geradas
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

## ▶️ Execução do Projeto

1. **Clone e instale dependências**

```bash
   git clone https://github.com/CahuVictor/PreferencIA.git
   poetry install
```

### 🐍 Ambiente Python com Poetry

O projeto utiliza o Poetry. Para instruções completas de instalação e ativação do ambiente, consulte o arquivo [`AMBIENTE_POETRY.md`](./docs/AMBIENTE_POETRY.md).

2. **Ative o ambiente Virtual**

Ative o ambiente virtual via `poetry shell`.

3. **Selecione como será o upload dos dados**

No `main.py`, existe uma variável chamada de `project_number` que define qual será o projeto utilizado, é influenciado pela forma como o sistema recebe os dados e a estrutura dos dados, atualmente no sistema tem as seguintes formas:

* **Upload via API**: Quando alterada a variável project_number para 1, é esperado o dado das URL `https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/`, os dados da API precisam pouco pré-processamento para gerar o dataset para treinar o modelo.
* **Upload via pasta \data**: Quando alterada a variável project_number para 2, é esperado os arquivos `BX-Book-Ratings.csv` e `BX-Books.csv` na pasta `/data`, e estes dados precisam de várias etapas de pré-processamento para gerar o dataset para treinar o modelo.

4. **Execute a aplicação**

```bash
python src/main.py --user_id 1 --top_n 5
```

5. **Coletando os resultados**

Você verá na tela uma lista de livros recomendados para o usuário especificado, além da criação de um arquivo `.csv` com as recomendações.

---

## Meta

Evoluir o projeto para que a aplicação seja uma chamada dessa forma

```bash
poetry run python src/main.py --ratings data/ratings.csv \
                              --min-user-ratings 50 \
                              --topn 5 \
                              --user 42
```

O processamento dos dados para gerar `ratings.csv` não deveria ser escopo dessa API

Uma alternativa seria algo assim

```bash
poetry run python src/main.py --ratings funcao_Aux(data/ratings.csv) \
                              --min-user-ratings 50 \
                              --topn 5 \
                              --user 42
```

---

## 📄 Documentação Adicional

* [Explicação detalhada do projeto e do código](./docs/EXPLICACAO_PROJETO.md)
* [Como configurar o VS Code para usar PowerShell](./docs/CONFIGURAR_VSCODE_POWERSHELL.md)

---

Mantenha seu ambiente sempre sincronizado com `poetry install` caso novas dependências sejam adicionadas.

---

## 🗺️ Roadmap

* Atualizar API para ser menos dependente dos dados csv
* Otimização de hiperparâmetros via RandomizedSearchCV
* Métricas offline adicionais (MAP, NDCG, cobertura, novidade)
* API REST com FastAPI para servir recomendações em tempo real
* Dashboard em Streamlit para exploração interativa das sugestões
* Suporte a datasets implícitos (feedback positivo/negativo)

---

## 🤝 Contribuindo

Pull requests são muito bem-vindos! Se quiser reportar bugs ou sugerir funcionalidades, abra uma issue.

* Fork o repositório
* Crie uma branch (git checkout -b feature/minha-melhor-melhor)
* Commit suas alterações (git commit -m 'feat: minha melhoria')
* Faça push (git push origin feature/minha-melhor-melhor)
* Abra um Pull Request

---