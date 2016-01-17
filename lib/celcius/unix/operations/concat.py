def concat_commands(commands):
    """Join UNIX commands with concat operator"""
    return '; '.join(commands)

def build_and_concat_commands(commands):
    """Build out commands before joining with concat operator"""
    built_commands = [x.build_command() for x in commands]
    return concat_commands(built_commands)
