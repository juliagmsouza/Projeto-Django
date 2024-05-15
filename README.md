# Sistema de Gerenciamento de Alunos

Este é um projeto Django que implementa um sistema de gerenciamento de alunos, permitindo criar, listar, atualizar e excluir registros de alunos. A aplicação também oferece endpoints para autenticação de usuários, permitindo o acesso seguro aos recursos da API.

## Documentação da API

A documentação completa da API pode ser encontrada no arquivo `docs.yaml` dentro da pasta `docs`. Este arquivo está no formato OpenAPI 3.0 (anteriormente conhecido como Swagger), que descreve todos os endpoints da API, os parâmetros esperados, as respostas possíveis e outros detalhes de implementação.

Para visualizar a documentação da API, abra o arquivo `docs.yaml` com um editor de texto ou utilize ferramentas online para visualização de especificações OpenAPI, como o Swagger Editor ou o Swagger UI.

1. Instale as dependências do Python listadas no arquivo `requirements.txt`:

2. Execute as migrações do banco de dados:

```
python manage.py migrate
```

3. Inicie o servidor de desenvolvimento:

```
python manage.py runserver
```