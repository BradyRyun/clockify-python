from clockify.clockify import Clockify
from pprint import pprint 

clockify_server = Clockify("XcN5OMhbvm/92koz")

workspace = "5dd88d841ca53362a488c45d"

x = clockify_server.create_new_project(workspace, "projeto")
pprint (x.__dict__)
