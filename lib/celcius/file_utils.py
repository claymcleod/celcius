import os, json, subprocess

celcius_config = None
home_path = '~'
env_home_path = os.environ.get('HOME')
if env_home_path != None:
    home_path = env_home_path

dot_celcius_folder = os.path.join(home_path, '.celcius')
config_file = os.path.join(dot_celcius_folder, 'config.json')
if os.path.exists(config_file):
    with open(config_file, 'r') as f:
        celcius_config = json.load(f)

def command_exists(command):
    try:
        p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()

        if 'not found' in out or 'not found' in err:
            return False

        return True
    except:
        return False

def get_celcius_config():
    return celcius_config
