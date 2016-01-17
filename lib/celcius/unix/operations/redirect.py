def redirect_output(commandstr, filename):
    """Redirect output of command"""
    return '{} > {}'.format(commandstr, filename)

def build_command_and_redirect_output(command, filename):
    """Build command and redirect output"""
    return ' > '.join([command.build_command(), filename])
