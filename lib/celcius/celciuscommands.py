"""All commands offered by Celcius for data pipelining.

This module contains all methods that string together
UNIX utilities to perform a specific task.
"""
import os, sys, json
from celcius import file_utils
from celcius.cmds import wget, curl, diff, concat, redirect, rm, mv, touch

def build_watch_url_and_append_command(urllocation, filelocation):
    """Build a command to watch a specific remote url and
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
    full_cmd = concat.concat_commands([touch.touch_file(filelocation), redirect_cmd, rm.rm_file(tmp_filelocation), rm.rm_file(filelocation), mv.move_file(new_filelocation, filelocation)])

    return full_cmd
