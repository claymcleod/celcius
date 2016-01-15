from celcius import celciuscommands

cmd = celciuscommands.build_watch_file_and_append_command('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', '~/.celcius/iris.csv')
print(cmd)
