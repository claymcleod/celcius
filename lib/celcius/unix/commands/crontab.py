from celcius.utils import cron_utils

class crontab(object):
    """Class wrapping the UNIX 'crontab' utility"""

    def __init__(self, command, jobid=""):
        self._command = command
        self._jobid = jobid

        # Time modifiers
        self._hour = '*'
        self._minute = '*'
        self._day_of_week = '*'
        self._day_of_month = '*'
        self._month_of_year = '*'

    def minute(self, minute):
        """Manually set the 'minute' time modifier"""
        self._minute = minute

    def hour(self, hour):
        """Manually set the 'hour' time modifier"""
        self._hour = hour

    def day_of_month(self, day_of_month):
        """Manually set the 'day_of_month' time modifier"""
        self._day_of_month = day_of_month

    def month_of_year(self, month_of_year):
        """Manually set the 'month_of_year' time modifier"""
        self._month_of_year = month_of_year

    def day_of_week(self, day_of_week):
        """Manually set the 'day_of_week' time modifier"""
        self._day_of_week = day_of_week

    def build_command(self):
        """Build out the crontab command"""
        return cron_utils.cronify("crontab -l | {{ cat; echo \"{} {} {} {} {} CJOBID='{}' MAILTO='' {}\"; }} | crontab - > /dev/null".format(self._minute, self._hour, self._day_of_month, self._month_of_year, self._day_of_week, self._jobid, self._command))
