import re
import logging
logging.basicConfig(level=logging.INFO)
from .abstract_clockify import AbstractClockify
# Represents time spent on a Task by a User

def validate_iso8601(str_val):
    regex = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$'
    match_iso8601 = re.compile(regex).match
    try:
        if match_iso8601( str_val ) is not None:
            return True
    except:
        pass
    return False


def validate_start_and_end(end, start):
    start_validate = validate_iso8601(start)
    end_validate = validate_iso8601(end)
    if not start_validate:
        logging.error("Invalid start date")
        raise ValueError("Please specify a valid ISO-8601 value for start date")
    if not end_validate:
        logging.error("Invalid end date")
        raise ValueError("Please specify a valid ISO-8601 value for end date")


def generate_time_entry_list(time_entries):
    time_entries_list = []
    for time_entry in time_entries:
        for te in time_entry:
            time_entries_list.append(te)
    return time_entries_list


class TimeEntry(AbstractClockify):
    
    def __init__(self,api_key):
        super(TimeEntry,self).__init__(api_key=api_key)

    # returns all time entry
    def get_all_time_entry_user(self,workspace_id,user_id): 
        try:
            logging.info("Start function: get_all_time_entry_user")
            url = self.base_url+'workspaces/'+workspace_id+'/user/'+user_id+'/time-entries'
            r = self.request_get(url)
            logging.info(r)
            return r
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)

    def get_all_time_entries_for_user_in_date_range(self,workspace_id,user_id,start,end):
        try:
            validate_start_and_end(end, start)
            logging.info("Start function: get_all_time_entries_for_user_in_date_range")
            url = self.base_url+'workspaces/'+workspace_id+'/user/'+user_id+'/time-entries'
            params = {
                "start": start,
                "end": end
            }
            r = self.request_get_params(url,params=params)
            logging.info(r)
            return r
        except ValueError as ve:
            logging.error("Please specify a proper start and end date")
        except Exception as e:
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)

    def get_all_time_entries_for_user_for_project_in_date_range(self,workspace_id,user_id,start,end,project_id):
        try:
            validate_start_and_end(end, start)
            logging.info("Start function: get_all_time_entries_for_user_for_project_in_date_range")
            url = self.base_url+'workspaces/'+workspace_id+'/user/'+user_id+'/time-entries'
            params = {
                "start": start,
                "end": end,
                "project": project_id
            }
            r = self.request_get_params(url,params=params)
            logging.info(r)
            return r
        except ValueError as ve:
            logging.error("Please specify a proper start and end date")
        except Exception as e:
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)
