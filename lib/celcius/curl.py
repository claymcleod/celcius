# -*- coding: utf-8 -*-
#
# Copyright © 2016 Clay L. McLeod <clay.l.mcleod@gmail.com>
#
# Distributed under terms of the MIT license.

from __future__ import print_function

class curl(object):

    options = []
    basecommand = 'curl'

    def __init__(self, urllocation=''):
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

    def print_command(self):
        print(self.build_command())

def build_download_file_command(urllocation, outputlocation):
    curl_cmd = curl(urllocation)
    curl_cmd.add_option('-s')
    curl_cmd.add_option('-o {}'.format(outputlocation))
    return curl_cmd

def build_file_to_stdout_command(urllocation):
    curl_cmd = curl(urllocation)
    curl_cmd.add_option('-s')
    return curl_cmd
