from datetime import datetime
from message_base import send_love_message


from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()

# Schedule job_function to be called every two seconds
sched.add_job(send_love_message, 'interval', seconds=10)
sched.start()