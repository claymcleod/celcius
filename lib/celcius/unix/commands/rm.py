class rm(object):
    """Class for wrapping UNIX 'rm' command"""

    basecommand = 'rm'

    def __init__(self, filename=''):
        self.options = []
        self.filename = filename

    def add_option(self, option):
        self.options.append(option)

    def build_command(self):
        command_bits = []
        command_bits.append(self.basecommand)

        if self.options != []:
            command_bits.append(' '.join(self.options))

        command_bits.append(self.filename)
        return ' '.join(command_bits)

def build_force_rm_command(filename):
    cmd = rm(filename)
    cmd.add_option("-f")
    return cmd
