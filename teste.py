from clockify.clockify import Clockify
from pprint import pprint 
clockify_server = Clockify("W/HtkbB5hxdlYvnp")
import datetime 
workspaces = clockify_server.get_all_workspaces()

for workspace in workspaces:
    #pprint (workspace)
    users = clockify_server.get_all_workspace_users(workspace['id'])
    for user in users:
        pprint (user['name'])
        pprint ("xxxxxxxxxxxxxxxx")
        times = clockify_server.get_all_time_entry_user(workspace['id'], user['id'])
        for time in times:
            start = str(time['timeInterval']['start'])
            end = str(time['timeInterval']['end'])
            if start is not None:
                start = datetime.datetime.strptime(start, '%Y-%m-%dT%H:%M:%SZ')
            if end is not None:
                end = datetime.datetime.strptime(end, '%Y-%m-%dT%H:%M:%SZ')
            pprint (end -start)
        