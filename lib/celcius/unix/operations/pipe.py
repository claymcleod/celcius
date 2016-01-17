def pipe_commands(commands):
    """Pipe commands together"""
    return ' | '.join(commands)

def build_and_pipe_commands(commands):
    """Command to build then pipe commands together"""
    built_commands = [x.build_command() for x in commands]
    return pipe_commands(built_commands)
