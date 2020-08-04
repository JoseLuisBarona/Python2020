# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 22:05:23 2020

@author: Barona
"""


class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
            v = self.s[self.i]
            self.i += 1
            return v

for x in I():
    print(x, end='')