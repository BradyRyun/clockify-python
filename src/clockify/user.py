import logging
logging.basicConfig(level=logging.INFO)
from .abstract_clockify import AbstractClockify
# An user
class User(AbstractClockify):

	def __init__(self,api_key):
		super(User,self).__init__(api_key=api_key)
		
	
	# returns all users
	def get_user(self,id): 
		try:
			logging.info("Start function: get_user")
			
			url = self.base_url + 'users/'+str(id)
            return self.request_get(url)
			
		except Exception as e: 
			logging.error("OS error: {0}".format(e))
			logging.error(e.__dict__) 
	
	# returns all users from a workspace
	def get_all_workspace_users(self,workspace_id): 
		try:
			logging.info("Start function: get_all_workspace_users")
			#TO DO
			raise Exception('TO DO', 'TO DO')			
			logging.info("End function: get_all_workspace_users")
		except Exception as e: 
			logging.error("OS error: {0}".format(e))
			logging.error(e.__dict__) 
	
	# add new user in a workspace
	def add_new_user(self,workspace_id,email): 
		try:
			logging.info("Start function: add_new_user")
			#TO DO
			raise Exception('TO DO', 'TO DO')			
			logging.info("End function: add_new_user")
		except Exception as e: 
			logging.error("OS error: {0}".format(e))
			logging.error(e.__dict__) 
