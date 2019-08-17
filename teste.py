from clockify.clockify import Clockify
from pprint import pprint 
clockify_server = Clockify("W/HtkbB5hxdlYvnp")

workspaces = clockify_server.get_all_workspaces()

for workspace in workspaces:
    pprint (workspace)
    #users = clockify_server.get_all_workspace_users(workspace['id'])
    #for user in users:
    #    times = clockify_server.get_all_time_entry_user(workspace['id'], user['id'])
    #    pprint (times)