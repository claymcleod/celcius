def ampersand_commands(commands):
    """Join UNIX commands together with an ampersand"""
    return ' && '.join(commands)

def build_and_ampersand_commands(commands):
    """Build out commands before joining them with an ampersand"""
    built_commands = [x.build_command() for x in commands]
    return ampersand_commands(built_commands)
