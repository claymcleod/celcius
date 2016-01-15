def pipe_and_build_commands(commands):
    built_commands = [x.build_command() for x in commands]
    return ' | '.join(built_commands)
