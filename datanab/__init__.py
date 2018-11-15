from .constants import *

class dotdict(dict):
    __getattr__ = dict.get

    def __repr__(self):
        return "{} {} \n ".format(self['value'],self['units'])
