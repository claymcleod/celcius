import subprocess

def get_all_celcius_commands():
    """Query cron for all celcius commands"""
    p = subprocess.Popen(["crontab", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return [x for x in out.split('\n') if 'CJOBID' in x]


def cronify(string):
    """Prepare normal commands for cron"""
    return string.replace('%', '\%')
