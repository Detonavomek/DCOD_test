# -*- coding: utf-8 -*-
__author__ = 'torvald'

import json

DATA = "data"
STRUCTURE = "structure"


class Parser(object):
    def __init__(self, filepath):
        self.file = filepath
        self.data, self.structure = self.parse()

    def parse(self):
        data, structure = [], []
        try:
            with open(self.file) as f:
                content = json.load(f)
                data = content[DATA]
                structure = content[STRUCTURE]
        except ValueError, e:
            print e
        finally:
            return data, structure

    @classmethod
    def get_from_file(cls, filepath):
        parser = cls(filepath)
        return parser.data, parser.structure
