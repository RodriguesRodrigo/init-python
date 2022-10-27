# init-python

Configuração inicial para projetos Python utilizando FastAPI.

# Configurando projeto

Crie e ative sua virtualenv:

```
python -m venv venv
source venv/bin/activate
```

Instale as dependências:

```
pip install -r requirements.txt
```

Por fim, rode o projeto:

```
uvicorn src.main:app --reload
```

Ao finalizar a configuração será possível acessar o projeto através da URL http://127.0.0.1:8000/healthcheck/
