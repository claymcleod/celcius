class diff(object):

    basecommand = 'diff'

    def __init__(self, fileone='', filetwo=''):
        self.options = []
        self.fileone = fileone
        self.filetwo = filetwo

    def add_option(self, option):
        self.options.append(option)

    def build_command(self):
        command_bits = []
        command_bits.append(self.basecommand)

        if self.options != []:
            command_bits.append(' '.join(self.options))

        command_bits.append(self.fileone)
        command_bits.append(self.filetwo)
        return ' '.join(command_bits)

def build_append_file_command(fileone, filetwo):
    diff_cmd = diff(fileone, filetwo)
    diff_cmd.add_option("--line-format='%L'")
    return diff_cmd
