from parsers.datalog.datalog_parser import DatalogParser

from ..asp.symbolic_constant import SymbolicConstant
from ..mapper import Mapper


class DatalogMapper(Mapper):
    """Contains methods used to transform Objects into program strings, which in turn can be appended to InputProgram
    objects. """

    __instance = None

    def __init__(self):
        if DatalogMapper.__instance:
            raise("Instance already exists")
        super(DatalogMapper, self).__init__()

    @classmethod
    def get_instance(cls):
        """Return the instance of DatalogMapper."""
        if not cls.__instance:
            cls.__instance = DatalogMapper()
        return cls.__instance

    def _get_actual_string(self, predicate, parameters_map):
        """Return a string representing atom, from given predicate name,
        and set of parameters."""
        atom = predicate + "("
        for i in range(0, len(parameters_map)):
            if i != 0:
                atom += ","
            object_term = parameters_map[i]
            if object_term is None:
                raise("Wrong term number of predicate " + predicate)
            if isinstance(object_term, int):
                atom += str(object_term)
            elif isinstance(object_term, SymbolicConstant):
                atom += str(SymbolicConstant(object_term))
            else:
                atom += "\"" + str(object_term) + "\""
        atom += ")"
        return atom

    def _get_id(self, atom):
        """Return a string representing a predicate."""
        if '(' not in atom:
            return atom

        return atom[:atom.index('(')]

    def _get_param(self, atom):
        """Return a set of parameter string name."""
        return DatalogParser.parse_parameters_from_atom(atom)
