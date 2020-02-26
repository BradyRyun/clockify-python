from clockify.clockify import Clockify
from pprint import pprint 

clockify_server = Clockify("xxxxxxxx")
wok_id = "5be0caaab079873ca2da70e5"
projects_clockify = clockify_server.get_all_projects(wok_id)
for project in projects_clockify:
    pprint (project['name'])
    tasks_done = clockify_server.get_task_done(wok_id, project['id'])
    tasks_active = clockify_server.get_task_active(wok_id, project['id'])
    pprint ("DONE: "+str(len(tasks_done)))
    pprint ("ACTIVE: "+str(len(tasks_active)))

                        