import datetime
import time

def delay_time(days):
    current_time = datetime.datetime.now()
    
    delay_miliseconds = 24*60*60*1000 * days
    
    current_time_timestap_miliseconds = (time.mktime(current_time.timetuple()))*1000

    return current_time_timestap_miliseconds - delay_miliseconds