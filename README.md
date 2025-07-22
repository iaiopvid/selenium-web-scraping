# 🕵️‍♂️ Desafio Fidelity - SPV Bot

Este projeto realiza consultas automatizadas em plataformas de Tribunal Jurídico utilizando Selenium, com dados armazenados em um banco MariaDB e/ou Postegres.

---

## 📦 Requisitos

- Python 3.10+
- MariaDB Server (local ou remoto)
- Google Chrome ou Microsoft Edge instalado
- `chromedriver` ou `msedgedriver` compatível com sua versão do navegador

---

## ⚙️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/spv-bot.git
cd spv-bot
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure o banco de dados (MariaDB) e ajuste a conexão no arquivo:

```
core/database/config.py
```

4. Certifique-se de que o `msedgedriver.exe` ou `chromedriver.exe` esteja disponível no PATH ou no mesmo diretório do script.

---

## 🚀 Execução

Para rodar o bot continuamente:

```bash
python main.py
```

Opcional: Para rodar o bot num ciclo completo de 0 a 3 e encerrar:

```bash
python _main.py
```

O script irá:
- Buscar pesquisas pendentes por filtros de 0 a 3
- Realizar buscas automatizadas via navegador
- Salvar os resultados no banco
- Repetir o processo de forma contínua

---

## 🧪 Estrutura de Pastas

```
.
├── core/
│   ├── database/           # Conexão com banco MariaDB
│   └── enums/              # Enum para tipos de resultados
├── documentos     
│   └── msedgedriver.exe    # Driver do MS Edge
├── domain/                 # Modelos de domínio (Pesquisas)
├── repository/             # Acesso ao banco (Pesquisas)
├── services/               # Regras de negócio e processamento
├── web/                    # Automação com Selenium
├── requirements.txt
└── main.py                 # Script principal
```

---

## 🐞 Logs e Debug

O sistema imprime logs no terminal, incluindo:
- Filtro sendo processado
- Resultado encontrado
- Status da repetição

---

## ✍️ Objeto

Desenvolvido para uso interno técnico com foco em automação jurídica e boas práticas Python (SOLID, Clean Code).

---