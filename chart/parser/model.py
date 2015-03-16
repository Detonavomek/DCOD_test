# -*- coding: utf-8 -*-
__author__ = 'torvald'

import json


class Parser(object):
    def __init__(self, file_path):
        self.file = file_path
        # self.

    def parse(self):
        with open(self.file) as f:
            return json.load(f)


    @classmethod
    def get_from_file(cls, file):
        parser = cls(file)
        return