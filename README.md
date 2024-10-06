# CSV Reader 1.0
#### Visão Geral
Bem vindo ao CSV Reader, script para leitura de emails em arquivos CSV através de um menu interativo com filtros por dominio.
Suas funcionalidades são:

- Listar todos os dados.
- Filtar dados dos usuários pelo domino Ex: '@gmail.com'.

Acesse: https://github.com/dezoliveira/csv-reader

---
#### Tecnologias 
- Python

#### Funções
- menu: chama o menu interativo e permite escolher uma opção para prosseguir
    - Opções
        - listar_dados: opção 1 de listagem de dados
        - filtro_por_dominio: opção 2 para filtro por dominio

    - Validações
        - valida_arquivo_csv: valida se arquivo csv existe

    - Listagens
        - listar_emails: função que chama as outras listagens conforme o filtro.
        - listar_todos_emails: lista todos os emails (sem filtro)
        - listar_emails_por_dominio: lista todos os usuarios com o dominio inserido(com filtro)

--- 
#### Como Rodar o Projeto (local)
- git clone https://www.github.com/dezoliveira/csv-reader
- cd csv-reader
- python script.py

#### Ler outro arquivo CSV
- Para ler outro arquivo csv você deverá:
    - Colocar o arquivo csv dentra da pasta raiz do projeto
    - Renomear o arquivo para dados.csv
