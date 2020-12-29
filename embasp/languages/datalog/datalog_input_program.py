from ...base.input_program import InputProgram
from .datalog_mapper import DatalogMapper


class DatalogInputProgram(InputProgram):
    """ This class models a generic Datalog input program.
        It provides the user with the possibility to add a fact to the program in the form of an annotated object.
    """

    def __init__(self):
        super(DatalogInputProgram, self).__init__()

    def add_object_input(self, input_obj):
        """Transforms a properly-annotated object into a program string (a fact) and appends it to current _programs.

        The parameter input_obj is an object to be transformed.
        """
        self.add_program(
            DatalogMapper.get_instance().get_string(input_obj) + ".")

    def add_objects_input(self, input_objs):
        """Transforms a set of objects."""
        for inputObj in input_objs:
            self.add_object_input(inputObj)
