# 🐍 Ambiente Python com Poetry

Este guia descreve como configurar e utilizar o ambiente virtual do projeto **PreferencIA** utilizando o **Poetry** no Windows para gerenciamento de dependências e ambientes virtuais.

---

## ✅ Pré-requisitos

* **Python 3.11** instalado.
  Caso não tenha, instale pelo **winget**:

  ```powershell
  winget install --id Python.Python.3.11 -e
  ```

* Terminal **PowerShell** ou **CMD**.

---

## 🔧 Instalação do Poetry

Para instalar o Poetry, execute no terminal:

```bash
pip install poetry
```

Após a instalação, **feche e reabra o terminal**, ou rode:

```powershell
$env:PATH += ";$HOME\AppData\Roaming\Python\Scripts"
```

Verifique se a instalação foi concluída corretamente:

```bash
poetry --version
```

---

## 🧩 Ativar o plugin `shell` (opcional, mas recomendado)

Por padrão, o comando `poetry shell` **não está disponível** no Poetry 2.x. Para habilitar:

```bash
poetry self add poetry-plugin-shell
```

Se ocorrer erro, pode ser por dois motivos:

Se estiver rodando no cmd, ou utilizando o VS Code e o VS Code esteja rodando o cmd, feche e **abra o Wndows Power Shell** e tente novamente.

Se continuar o erro, pode ser erro de permissão, **abra o terminal como Administrador** e tente novamente.

---

## 📦 Instalar as dependências e criar o ambiente virtual

Dentro da pasta do projeto:

Se foi instalado o **Python 3.11** via **winget** faça:

```powershell
# 1) crie um venv explícito em Python 3.11
py -3.11 -m venv .venv

# 2) peça ao Poetry para usar esse venv
poetry env use .\.venv\Scripts\python.exe

# 3) instale as dependências definidas no poetry.lock
poetry install
```

Se foi instalado o Python 3.11 de forma tradicional na máquina, faça:

```bash
poetry install
```

---

## 🚀 Ativar o ambiente virtual

Se você ativou o plugin `shell`, use:

```bash
poetry shell
```

Se não estiver usando o plugin, ative o ambiente diretamente:

```bash
poetry env info --path
```

Copie o caminho retornado e ative manualmente no PowerShell ou CMD:

```bash
# Exemplo no PowerShell
& "C:\Users\Aluno\AppData\Local\pypoetry\Cache\virtualenvs\pos-jSRnZJkA-py3.11\Scripts\activate"
```

ou

```powershell
.\.venv\Scripts\activate
```

---

## ▶️ Executar o projeto

Com o ambiente virtual ativado, execute o script principal do projeto com:

```bash
python recomendador.py`
```

---

## 📚 Bibliotecas utilizadas

| Biblioteca        | Versão     | Descrição                                                           |
|-------------------|------------|---------------------------------------------------------------------|
| `joblib`          | 1.5.1      | Pipelines leves com funções Python                                 |
| `numpy`           | 1.24.3     | Computação numérica com arrays                                     |
| `pandas`          | 2.0.3      | Estruturas de dados para análise estatística e séries temporais    |
| `python-dateutil` | 2.9.0.post0| Extensões para o módulo `datetime` do Python                       |
| `pytz`            | 2025.2     | Fuso horários históricos e atuais do mundo                         |
| `scikit-surprise` | 1.1.4      | Biblioteca para sistemas de recomendação                           |
| `scipy`           | 1.15.3     | Algoritmos científicos e estatísticos                              |
| `six`             | 1.17.0     | Compatibilidade entre Python 2 e 3                                 |
| `surprise`        | 0.1        | Biblioteca de recomendação baseada em fatoração de matrizes        |
| `tzdata`          | 2025.2     | Dados da IANA sobre fusos horários                                 |

---

Se tiver dúvidas sobre alguma etapa, abra uma *issue* ou entre em contato com os desenvolvedores do projeto.