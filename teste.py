from clockify.clockify import Clockify
from pprint import pprint 

clockify_server = Clockify("XcN5OMhbvm/92koz")

workspaces = clockify_server.get_all_workspaces()
workspaces = workspaces.json()

for workspace in workspaces:
    projects = clockify_server.get_all_projects(workspace['id'])
    pprint (workspace['name'])
    