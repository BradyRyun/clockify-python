from clockify import factories
from pprint import pprint

api_key = "Xlb9JuSKM2s1TwAk"
workspace_services = factories.WorkspaceFactory(api_key=api_key)
worspaces = workspace_services.get_all_workspaces()

for workspace in worspaces:
    pprint (workspace)