# Goal
It is reponsible for sending command to [Clockify API](https://clockify.me/).

This lib was build based on [API documentation](https://clockify.me/developers-api) da ferramenta.

## Installation
To install clockify, run this command in your terminal:
```
pip install clockify
```

## Usage
To use changelogs in a Python project:

```python
from clockify.clockify import Clockify
from pprint import pprint 
clockify_server = Clockify("chavedeacesso")
workspaces = clockify_server.get_all_workspaces()

for workspace in workspaces:
    pprint (workspace)
```