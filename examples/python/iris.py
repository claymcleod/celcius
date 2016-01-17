#! /usr/bin/env python

from __future__ import print_function

from celcius import tasks
from celcius.unix.commands.crontab import crontab

cmd = tasks.build_append_file_task('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', '~/.celcius/iris.csv')
cron_cmd = crontab(cmd)
print(cron_cmd.build_command())
