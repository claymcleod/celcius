class wget(object):

    basecommand = 'wget'

    def __init__(self, urllocation=''):
        self.options = []
        self.urllocation = urllocation

    def add_option(self, option):
        self.options.append(option)

    def build_command(self):
        command_bits = []
        command_bits.append(self.basecommand)

        if self.options != []:
            command_bits.append(' '.join(self.options))

        command_bits.append(self.urllocation)
        return ' '.join(command_bits)

def build_download_file_command(urllocation, outputlocation):
    wget_cmd = wget(urllocation)
    wget_cmd.add_option('-q')
    wget_cmd.add_option('-O {}'.format(outputlocation))
    return wget_cmd

def build_file_to_stdout_command(urllocation):
    wget_cmd = wget(urllocation)
    wget_cmd.add_option('-S')
    wget_cmd.add_option('-q')
    wget_cmd.add_option('-O -')
    return wget_cmd
