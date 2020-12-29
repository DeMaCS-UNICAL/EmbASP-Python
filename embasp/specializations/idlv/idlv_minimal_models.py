from ...languages.datalog.minimal_models import MinimalModels
from parsers.datalog.datalog_solvers_parser import DatalogSolversParser


class IDLVMinimalModels(MinimalModels):
    """Represents IDLV's minimal models."""

    def __init__(self, out, err=None):
        super(IDLVMinimalModels, self).__init__(out, err)

    def _parse(self):
        DatalogSolversParser.parse_idlv(self, self._output, True)
