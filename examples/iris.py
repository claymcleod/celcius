from celcius import celciuscommands
from celcius.crontab import crontab

cmd = celciuscommands.build_watch_file_and_append_command('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', '~/.celcius/iris.csv')
cron_cmd = crontab(cmd)
cron_cmd.print_command()
