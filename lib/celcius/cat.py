# -*- coding: utf-8 -*-
#
# Copyright © 2016 Clay L. McLeod <clay.l.mcleod@gmail.com>
#
# Distributed under terms of the MIT license.

from __future__ import print_function

class cat(object):

    options = []
    basecommand = 'cat'

    def __init__(self, filename=''):
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

    def print_command(self):
        print(self.build_command())
