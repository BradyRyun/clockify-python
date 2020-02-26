# Goal
It is reponsible for sending command to [Clockify API](https://clockify.me/).

This lib was built based on [Clockify API documentation](https://clockify.me/developers-api).

## Installation
To install clockify, run this command in your terminal:
```
pip install clockify
```

## Usage
To use clockify in a Python project:

```python
from clockify.clockify import Clockify
from pprint import pprint 
clockify_server = Clockify("secretkey")
workspaces = clockify_server.get_all_workspaces()

for workspace in workspaces:
    pprint (workspace)
```