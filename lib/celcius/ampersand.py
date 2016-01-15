def ampersand_commands(commands):
    return ' && '.join(commands)

def build_and_ampersand_commands(commands):
    built_commands = [x.build_command() for x in commands]
    return ampersand_commands(built_commands)
