# init-python

Configuração inicial para projetos Python utilizando FastAPI.

# Configurando projeto

Faça uma cópia do arquivo `.env.example` no mesmo diretório, renomeie o novo arquivo para `.env` e por fim fim modifique as variáveis de ambiente deste arquivo.

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

# Melhorias

- [ ] Configurar pytest
- [ ] Configurar pre-commit
- [ ] Configurar flake8
