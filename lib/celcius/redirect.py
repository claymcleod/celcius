def redirect_output(commandstr, filename):
    return '{} > {}'.format(commandstr, filename)

def build_command_and_redirect_output(command, filename):
    return ' > '.join([command.build_command(), filename])
