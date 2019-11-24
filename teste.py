from clockify.clockify import Clockify
from pprint import pprint 

clockify_server = Clockify("XcN5OMhbvm/92koz")

workspace = "5dda7fc31ca53362a48b291e"

x = clockify_server.add_new_user(workspace, "paulo.junior@ifes.edu.br")
pprint (x.__dict__)
