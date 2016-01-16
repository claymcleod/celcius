# -*- coding: utf-8 -*-
#
# Copyright © 2016 Clay L. McLeod <clay.l.mcleod@gmail.com>
#
# Distributed under terms of the MIT license.

from __future__ import print_function

class diff(object):

    options = []
    basecommand = 'diff'

    def __init__(self, fileone='', filetwo=''):
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

    def print_command(self):
        print(self.build_command())

def build_append_file_command(fileone, filetwo):
    diff_cmd = diff(fileone, filetwo)
    diff_cmd.add_option("--line-format='%L'")
    return diff_cmd
