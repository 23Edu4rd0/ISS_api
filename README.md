# ISS_api

Projeto Python para monitoramento da Estação Espacial Internacional (ISS) e envio de e-mail quando a ISS estiver visível na sua cidade.

## Funcionalidades

- Consulta a posição atual da ISS via API.
- Consulta horários de nascer e pôr do sol para sua localização.
- Compara se a ISS está próxima e visível no céu da sua cidade.
- Envia um e-mail HTML informando se a ISS está visível ou não, incluindo a posição atual da ISS.

## Estrutura do Projeto

```
ISS_api/
├── main.py
├── models/
│   ├── location.py
│   └── iss_location.py
├── services/
│   ├── iss_api.py
│   ├── iss_comparator.py
│   └── sunrise_sunset_api.py
├── utils/
│   └── email_sender.py
├── requirements.txt
├── Dockerfile
└── .gitignore
```

## Como usar

### 1. Clonar o repositório

```sh
git clone https://github.com/seu_usuario/ISS_api.git
cd ISS_api
```

### 2. Configurar variáveis de e-mail

Edite o arquivo `utils/email_sender.py` e coloque seu e-mail e senha de app nas variáveis `from_email` e `password`.

### 3. Instalar dependências

**Com ambiente virtual:**
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Ou usando Docker:**
```sh
docker build -t iss_api .
docker run --rm iss_api
```

### 4. Executar o projeto

```sh
python main.py
```

## Observações

- Para envio de e-mail pelo Gmail, use uma senha de app (não sua senha normal).
- O projeto pode ser facilmente adaptado para outras localizações, basta alterar as coordenadas em `main.py` ou nos arquivos de configuração.
- O tempo de execução é exibido ao final do script.

