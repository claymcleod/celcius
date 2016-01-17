class cat(object):
    """Class for wrapping UNIX 'cat' command"""

    basecommand = 'cat'

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
