from abc import ABCMeta, abstractmethod


class DatalogDataCollection(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def add_minimal_model(self):
        pass
