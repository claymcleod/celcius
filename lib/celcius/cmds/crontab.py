import subprocess

def cronify(string):
    return string.replace('%', '\%')

def get_all_celcius_commands():
    p = subprocess.Popen(["crontab", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return [x for x in out.split('\n') if 'CJOBID' in x]

class crontab(object):
    _minute = '*'
    _hour = '*'
    _day_of_month = '*'
    _month_of_year = '*'
    _day_of_week = '*'
    _command = ''

    def __init__(self, command, jobid=""):
        self._command = command
        self._jobid = jobid

    def minute(self, minute):
        assert isinstance(minute, int)
        self._minute = str(minute)

    def hour(self, hour):
        assert isinstance(hour, int)
        self._hour = str(hour)

    def day_of_month(self, day_of_month):
        assert isinstance(day_of_month, int)
        self._day_of_month = str(day_of_month)

    def month_of_year(self, month_of_year):
        assert isinstance(month_of_year, int)
        self._month_of_year = str(month_of_year)

    def day_of_week(self, day_of_week):
        assert isinstance(day_of_week, int)
        self._day_of_week = str(day_of_week)

    def build_command(self):
        return cronify("crontab -l | {{ cat; echo \"{} {} {} {} {} CJOBID='{}' MAILTO='' {}\"; }} | crontab -".format(self._minute, self._hour, self._day_of_month, self._month_of_year, self._day_of_week, self._jobid, self._command))

    def print_command(self):
        print(self.build_command())
