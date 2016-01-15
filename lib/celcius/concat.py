def concat_commands(commands):
    return '; '.join(commands)

def build_and_concat_commands(commands):
    built_commands = [x.build_command() for x in commands]
    return concat_commands(built_commands)
