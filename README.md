#  API de Gerenciamento de Produtos - E-commerce

##  Tecnologias Utilizadas

* **FastAPI:** Framework web moderno e de alto desempenho para construir APIs com Python.
* **SQLAlchemy:** ORM para mapeamento e manipulação do banco de dados.
* **Pydantic V2:** Validação de dados e definições de schemas.
* **PostgreSQL:** Banco de dados relacional para persistência de dados.
* **Docker & Docker Compose:** Containerização da aplicação e dos serviços de banco de dados.
* **Pytest & Pytest-Cov:** Framework de testes e relatório de cobertura de código.

---

##  Arquitetura do Projeto

O projeto adota uma estrutura modular e dividida em responsabilidades claras dentro da pasta `app/`:


├── app/
│   ├── routes.py          # Camada de Endpoints (HTTP Requests/Responses)
│   ├── services.py        # Camada de Regras de Negócio
│   ├── repositories.py    # Camada de Acesso ao Banco de Dados (Consultas SQL)
│   ├── models.py          # Modelos de Tabelas do SQLAlchemy
│   ├── schemas.py         # Schemas de Validação de Dados do Pydantic
│   ├── database.py        # Configuração da Sessão do Banco de Dados
│   └── config.py          # Gerenciamento de Variáveis de Ambiente
├── tests/                 # Suíte de Testes Automatizados com Pytest
├── .env.example           # Modelo das Variáveis de Ambiente
├── docker-compose.yml     # Configuração dos Containers PostgreSQL
├── pytest.ini             # Configurações do Ambiente de Testes
└── requirements.txt       # Dependências do Projeto


## Como Executar o Projeto

1. Clonar o Repositório

git clone <url-do-seu-repositorio>
cd P2BACKEND

2. Configurar as Variáveis de AmbienteCrie um arquivo .env na raiz do projeto baseado no modelo fornecido:Bashcp .env.example .env
(Abra o arquivo .env e ajuste as credenciais se achar necessário).

3. Subir os Bancos de Dados com DockerO projeto utiliza dois contêineres PostgreSQL isolados: um para desenvolvimento (porta 5432) e outro para os testes (porta 5433).
docker compose up -d

4. Configurar o Ambiente Virtual (Python)Bash# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual (Windows)
.\venv\Scripts\activate

# Instalar as dependências
pip install -r requirements.txt

5. Iniciar o Servidor da API
uvicorn app.main:app --reload

A API estará disponível em: http://127.0.0.1:8000
A documentação interativa (Swagger UI) estará em: http://127.0.0.1:8000/docs
Como Rodar os Testes e Cobertura
Os testes foram desenvolvidos utilizando o banco de dados volátil e isolado db_test (porta 5433) para garantir o isolamento total de estado entre execuções.
Para rodar todos os testes automatizados e verificar o relatório de cobertura de código (pytest-cov), execute o seguinte comando no seu terminal com o ambiente virtual ativo:
pytest --cov=app -v


 Relatório de Cobertura ObtidoO projeto atinge 96% de cobertura de código nos módulos do diretório app/, superando com folga a meta mínima exigida de 85%:
 app/routes.py: 100%
 app/services.py: 100%
 app/repositories.py: 100%
 app/models.py: 100%
 app/schemas.py: 100%
 
Endpoints Principais da API
Método,Endpoint,Descrição
POST, /produtos, Cria um novo produto no sistema.
GET, /produtos, Lista todos os produtos cadastrados e ativos.
GET, produtos/{id}, Busca os detalhes de um produto específico por ID.
DELETE, /produtos/{id}, Remove logicamente ou deleta um produto por ID.