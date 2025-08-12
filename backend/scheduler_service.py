import schedule
import time
from datetime import datetime

class SchedulerService():
    def __init__(self, task_provider):
        self.task_provider = task_provider

    def schedule_daily_task(self):

        schedule.every().day.at("9:00").do(self.task_provider.task())

    def run(self):
        print("Scheduler started. Press Ctrl+C to exit.")
        while True:
            schedule.run_pending()
            time.sleep(1)
