from clockify.clockify import Clockify
from pprint import pprint 
clockify_server = Clockify("Xlb9JuSKM2s1TwAk")
x = clockify_server.get_all_time_entry_user("5be0caaab079873ca2da70e5", "5be0caa9b079873ca2da70e2")