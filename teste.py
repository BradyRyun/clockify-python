from clockify.clockify import Clockify
from pprint import pprint 
clockify_server = Clockify("W/HtkbB5hxdlYvnp")

workspaces = clockify_server.get_all_workspaces()

for workspace in workspaces:
    pprint (workspace.name)
    id = workspace.id
    projects = clockify_server.get_all_projects(id)
    
    for project in projects:
        pprint ("Name:" +project['name'])
    
    pprint ("==================")
