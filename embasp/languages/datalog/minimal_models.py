from abc import ABCMeta

from parsers.datalog.datalog_data_collection import DatalogDataCollection

from ...base.output import Output
from .minimal_model import MinimalModel


class MinimalModels(Output, DatalogDataCollection):
    """A collection of Minimal Models."""
    __metaclass__ = ABCMeta

    def __init__(self, out, err=None):
        super(MinimalModels, self).__init__(out, err)
        self._minimal_models = None

    def get_minimal_models(self):
        """Return a set of MinimalModel objects."""
        if self._minimal_models is None:
            self._minimal_models = set()
            self._parse()
        return self._minimal_models

    def get_minimalmodels_as_string(self):
        """Return a string containing all models."""
        return self._output

    def add_minimal_model(self, minimal_model: MinimalModel):
        self._minimal_models.add(minimal_model)
