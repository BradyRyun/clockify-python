from clockify import factories
from pprint import pprint

api_key = "Xlb9JuSKM2s1TwAk"


workspace_services = factories.WorkspaceFactory(api_key=api_key)
project_services = factories.ProjectFactory(api_key=api_key)
tasks_services = factories.TaskFactory(api_key=api_key)
timeentry_services = factories.TimeEntryFactory(api_key=api_key)
user_services = factories.UserFactory(api_key=api_key)

worspaces = workspace_services.get_all_workspaces()
'''

for workspace in worspaces:
    pprint (workspace['name'])
    # First: Get the Workspace ID
    worspace_id = workspace['id']
    
    projects = project_services.get_all_projects(worspace_id)
    for project in projects:
        # Second: Get the Project ID
        pprint (project['name'])
        project_id = project['id']
        # Third: Get the Tasks ID
        tasks__done = tasks_services.get_task_done(worspace_id,project_id)
        tasks__active = tasks_services.get_task_active(worspace_id,project_id)
        for task__done in tasks__done:
            pprint (task__done)

        for task__active in tasks__active:
            pprint (task__active)
 '''   

for workspace in worspaces:
    pprint (workspace['name'])
    
    # First: Get the Workspace ID
    worspace_id = workspace['id']
    users = user_services.get_all_workspace_users(worspace_id)
    for user in users:
        user_id = user['id']
        # Second: Get the Workspace ID
        timeentries = timeentry_services.get_all_time_entry_user(worspace_id,user_id)
        if timeentries is not None:
            for time_entry in timeentries:
                pprint (time_entry)