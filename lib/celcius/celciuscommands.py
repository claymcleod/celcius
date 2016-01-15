import os, sys, json
from celcius import wget, curl, diff, concat, redirect, rm, mv

def build_watch_file_and_append_command(urllocation, filelocation):
    home_path = '~'
    env_home_path = os.environ.get('HOME')
    if env_home_path != None:
        home_path = env_home_path

    dot_celcius_folder = os.path.join(home_path, '.celcius')
    config_file = os.path.join(dot_celcius_folder, 'config.json')
    with open(config_file, 'r') as f:
        config = json.load(f)

    basename = filelocation.split('/')[-1]
    tmp_filelocation = filelocation.replace(basename, 'tmp_'+basename)
    new_filelocation = filelocation.replace(basename, 'new_'+basename)

    if config['retrieve_command'] == 'curl':
        download_cmd = wget.build_download_file_command(urllocation, tmp_filelocation)
    elif config['retrieve_command'] == 'wget':
        download_cmd = curl.build_download_file_command(urllocation, tmp_filelocation)
    else:
        print("Invalid retrieve command!")
        sys.exit(1)

    diff_cmd = diff.build_append_file_command(filelocation, tmp_filelocation)
    compare_cmd = concat.build_and_concat_commands([download_cmd, diff_cmd])
    redirect_cmd = redirect.redirect_output(compare_cmd, new_filelocation)
    full_cmd = concat.concat_commands([redirect_cmd, rm.rm_file(tmp_filelocation), rm.rm_file(filelocation), mv.move_file(new_filelocation, filelocation)])

    return full_cmd
