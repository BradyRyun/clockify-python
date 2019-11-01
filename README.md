# Objetivo
Biblioteca responsável por realizar operações (e.g., busca ou criação de projetos) no [clockify](https://clockify.me/).

A biblioteca foi construída tomando como base a [documentação](https://clockify.me/developers-api) da ferramenta.

## Instalação
pip install clockify


## Exemplo de utilização

```python
from clockify.clockify import Clockify
from pprint import pprint 
clockify_server = Clockify("chavedeacesso")
workspaces = clockify_server.get_all_workspaces()

for workspace in workspaces:
    pprint (workspace)
```