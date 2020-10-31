# Clockify

## General Information
* **Software**:clockify
* **Author**:Paulo Sérgio dos Santos Júnior
* **Author's e-mail**:paulossjunior@gmail.com
* **Source Repository**: [https://gitlab.com/integration_seon/libs/application/clockify](https://gitlab.com/integration_seon/libs/application/clockify)  

## Goal
Clockify is the only truly free time tracker and timesheet app for teams of all sizes. Unlike all the other time trackers, Clockify is available for an unlimited numbers of users for free

## Documentation

The Documentation can be found in this [link](./docs/documentation.md)

## Generate documentation

To create the code documentation:
```bash
pdoc --html --force clockify/ --output docs

```
### Acess code documentation	

To accesss the documenation, go to folder docs/clockify and open index.html 

	
## Instalation

To install clockify, run this command in your terminal:
```bash
pip install clockify
```

## Usage

```python

from clockify import factories
from pprint import pprint

api_key = "<personal _token>"
workspace_services = factories.WorkspaceFactory(api_key=api_key)
worspaces = workspace_services.get_all_workspaces()

for workspace in worspaces:
    pprint (workspace)
```

## Copyright
This lib was PowerRight by [SEON Application Lib Generator](https://gitlab.com/mdd_seon/from_application_conceptual_data_model_2_lib_application)

	
