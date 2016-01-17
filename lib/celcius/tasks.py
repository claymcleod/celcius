"""All tasks offered by Celcius for data pipelining.

This module contains all methods that string together
UNIX utilities to perform a specific task.
"""
import os, sys, json
from celcius.utils import file_utils
from celcius.unix.commands import wget, curl, diff, rm, mv, touch
from celcius.unix.operations import concat, redirect

def build_append_file_task(urllocation, filelocation):
    """Build a task to watch a specific remote url and
append that data to the file. This method should be used
when you would like to keep all of the information stored
on the local machine, but also append the new information
found at the url.

For instance, if the local file is:

```
foo
```

And the remote file is:

```
bar
```

The resulting file will contain:

```
foo
bar
```
    """

    config = file_utils.get_celcius_config()
    basename = filelocation.split('/')[-1]
    tmp_filelocation = filelocation.replace(basename, 'tmp_'+basename)
    new_filelocation = filelocation.replace(basename, 'new_'+basename)

    if config['retrieve_command'] == 'curl':
        download_cmd = curl.build_download_file_command(urllocation, tmp_filelocation)
    elif config['retrieve_command'] == 'wget':
        download_cmd = wget.build_download_file_command(urllocation, tmp_filelocation)
    else:
        print("Invalid retrieve command!")
        sys.exit(1)

    diff_cmd = diff.build_append_file_command(filelocation, tmp_filelocation)
    compare_cmd = concat.build_and_concat_commands([download_cmd, diff_cmd])
    redirect_cmd = redirect.redirect_output(compare_cmd, new_filelocation)
    full_cmd = concat.concat_commands([touch.touch(filelocation).build_command(), redirect_cmd, rm.build_force_rm_command(tmp_filelocation).build_command(), rm.build_force_rm_command(filelocation).build_command(), mv.mv(new_filelocation, filelocation).build_command()])

    return full_cmd


def build_replicate_file_task(urllocation, filelocation):

    config = file_utils.get_celcius_config()

    if config['retrieve_command'] == 'curl':
        download_cmd = curl.build_download_file_command(urllocation, filelocation)
    elif config['retrieve_command'] == 'wget':
        download_cmd = wget.build_download_file_command(urllocation, filelocation)
    else:
        print("Invalid retrieve command!")
        sys.exit(1)

    full_cmd = concat.concat_commands([rm.rm(filelocation).build_command(), download_cmd.build_command()])

    return full_cmd
