# Gemini Product Embedder
![Python](https://img.shields.io/badge/python-3.13-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

## 🔹 Sobre o Projeto

O Gemini Product Embedder é um projeto voltado para manipulação de dados de produtos. Ele recebe um arquivo JSON contendo produtos, insere os dados em um banco PostgreSQL e gera embeddings semânticos para cada produto, armazenando-os diretamente no banco.

O objetivo é criar uma base de dados enriquecida, preparada para análises futuras ou consultas inteligentes por similaridade, com embeddings de texto que representam as informações de cada produto.

---

## 🎯 Objetivo

- Ler produtos a partir de um arquivo JSON.
- Inserir produtos no banco PostgreSQL com checagem de duplicidade.
- Gerar embeddings semânticos para cada produto usando a API Gemini Embeddings.
- Armazenar os embeddings em uma coluna dedicada (`embedding`) para consultas futuras.
- Preparar a base para análises ou recomendações baseadas em semântica.

---

## 🛠 Tecnologias e Ferramentas

- **Python** 3.13
- **SQLAlchemy** para ORM e operações no banco
- **PgVector** para armazenamento vetorial
- **GeminiEmbedder** para geração de embeddings
- **PostgreSQL** com extensão pgvector
- **dotenv** para configuração de variáveis de ambiente
- **Docker Compose** para orquestração do banco

---

## ⚙️ Configuração do Projeto

1. Crie um **.venv**:
```bash

python -m venv .venv
```

2. Ative o **.venv**
- Windows
```bash

.venv\Scripts\activate
```
- Linux
```bash

source .venv/bin/activate
```

3. Instale as dependências:
```bash

pip install -r requirements.txt
```

4. Crie um arquivo **.env** na raiz do seu projeto seguindo o arquivo **.env.example** com suas chaves:

```
GOOGLE_API_KEY=your_api_key
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=your_db
DB_PORT=5432
```

5. Inicie o container com a imagem do pgvector e PostgreSQL:

```bash

docker compose up -d
```

---

## 🚀 Como Rodar

Execute no terminal:

```bash

python .\main.py
```

O script irá:

1. Conectar ao banco PostgreSQL.
2. Criar a tabela `products` caso não exista.
3. Ler produtos do JSON (`data/products.json`).
4. Gerar embeddings para cada produto.
5. Inserir os produtos no banco com os embeddings.


---

## 📝 Estrutura do Projeto

```bash

gemini-product-embedder/
│
├─ db/
│  ├─ connection.py
│  ├─ connection.py
│  └─ models.py
│
├─ embeddings/
│  └─ generate.py
│
├─ utils/
│  ├─ logger_config.py
│  └─ read_json_products.py
│
├─ data/
│  └─ products.json
│
├─ main.py
├─ docker-compose.yaml
├─ requirements.txt
├─ .env
└─ README.md

```

---

## ⚖️ Licença

Este projeto está licenciado sob a MIT License.
