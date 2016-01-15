class crontab(object):
    _minute = '*'
    _hour = '*'
    _day_of_month = '*'
    _month_of_year = '*'
    _day_of_week = '*'
    _year = '*'
    _command = ''

    def __init__(self, command):
        self._command = command

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

    def year(self, year):
        assert isinstance(year, int)
        self._year = str(year)

    def build_command(self):
        return "crontab -l | {{ cat; echo \"{} {} {} {} {} {} {}\"; }} | crontab -".format(str(self._minute), str(self._hour), str(self._day_of_month), str(self._month_of_year), str(self._day_of_week), str(self._year), str(self._command))

    def print_command(self):
        print(self.build_command())
