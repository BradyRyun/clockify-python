from clockify.clockify import Clockify
from pprint import pprint 
clockify_server = Clockify("XcN5OMhbvm/92koz")
import datetime 
workspaces = clockify_server.get_all_workspaces()

for workspace in workspaces:
    #pprint (workspace)
    users = clockify_server.get_all_workspace_users(workspace['id'])
    for user in users:
        pprint (user['name'])
        times = clockify_server.get_all_time_entry_user(workspace['id'], user['id'])
        for time in times:
            pprint (time)
            '''start = str(time['timeInterval']['start'])
            start = start.lstrip()
            end = str(time['timeInterval']['end'])
            end = end.lstrip()

            pprint ("ProjectID"+str(time['projectId']))
            pprint ("ID"+ sttime['id'])
            pprint ("UserId"+time['userId'])
            pprint ("Work"+ time['workspaceId'])
            pprint ("start"+ str(start))
            pprint ("end"+ str(end))
            
            if start is not None and start != 'None':
                start = datetime.datetime.strptime(start, '%Y-%m-%dT%H:%M:%SZ')
            if end is not None and end != 'None':
                end = datetime.datetime.strptime(end, '%Y-%m-%dT%H:%M:%SZ')
                pprint (end -start)
            '''