class curl(object):

    basecommand = 'curl'

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
    curl_cmd = curl(urllocation)
    curl_cmd.add_option('-s')
    curl_cmd.add_option('-o {}'.format(outputlocation))
    return curl_cmd

def build_file_to_stdout_command(urllocation):
    curl_cmd = curl(urllocation)
    curl_cmd.add_option('-s')
    return curl_cmd
