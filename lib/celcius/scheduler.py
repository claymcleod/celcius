import schedule

class scheduler(object):

    @staticmethod
    def get_all_jobs():
        return schedule.jobs
