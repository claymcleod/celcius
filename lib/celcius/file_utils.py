import subprocess

def command_exists(command):
    try:
        p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()

        if 'not found' in out or 'not found' in err:
            return False

        return True
    except:
        return False
