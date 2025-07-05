# ⚙️ Configurando o VS Code para usar PowerShell como Terminal Padrão

Este guia mostra como alterar o terminal padrão do **Visual Studio Code** no Windows, substituindo o **CMD** pelo **PowerShell**.

---

## 🧭 Passo a Passo

### ✅ 1. Abrir o Terminal Integrado

- Vá até o menu superior do VS Code:
  ```
  Terminal → New Terminal
  ```
  ou use o atalho:
  ```
  Ctrl + `
  ```

---

### ✅ 2. Selecionar o Perfil de Terminal Padrão

- Clique na **seta ao lado do botão "+"** no terminal.
- Escolha a opção:
  ```
  Select Default Profile
  ```
- Na lista que aparecer, selecione:
  ```
  PowerShell
  ```

> Caso o PowerShell não apareça, certifique-se de que ele está instalado no seu sistema.

---

### 🔁 3. Reiniciar o Terminal

- Feche o terminal atual (ícone de **lixeira** no canto superior direito do terminal).
- Abra um novo terminal novamente com:
  ```
  Ctrl + `
  ```

O terminal agora abrirá com o **PowerShell** como padrão.

---

## 🛠️ Alternativa: Configurar Manualmente via settings.json

1. Pressione:
   ```
   Ctrl + Shift + P
   ```
2. Digite:
   ```
   Preferences: Open Settings (JSON)
   ```
3. Adicione ou edite as seguintes linhas no arquivo `settings.json`:

```json
"terminal.integrated.defaultProfile.windows": "PowerShell",
"terminal.integrated.profiles.windows": {
  "PowerShell": {
    "source": "PowerShell",
    "icon": "terminal-powershell"
  }
}
```

---

## ✅ Resultado Esperado

A partir de agora, sempre que você abrir o terminal integrado no VS Code, ele será iniciado com o **PowerShell** em vez do CMD.

Se tiver dúvidas, acesse a [documentação oficial do VS Code](https://code.visualstudio.com/docs/terminal/basics).