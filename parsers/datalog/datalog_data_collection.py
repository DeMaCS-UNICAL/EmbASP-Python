from abc import ABCMeta, abstractmethod

from languages.datalog.minimal_model import MinimalModel


class DatalogDataCollection(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def add_minimal_model(self, minimal_model: MinimalModel):
        pass
