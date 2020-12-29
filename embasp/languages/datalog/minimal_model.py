from .datalog_mapper import DatalogMapper


class MinimalModel(object):
    """A collection of data representing a generic MinimalModel."""

    def __init__(self, value):

        # Where the string representation of the atoms is stored
        self.__atom_string_collection = value
        self.__atom_object_collection = set()  # Where model atoms are stored

    def get_atoms_as_stringlist(self):
        """Return the current __atom_string_collection data.

        The method returns a set of String objects, each representing a different atom of the model.
        """
        return self.__atom_string_collection

    def get_atoms_as_objectset(self):
        """Return atoms stored in __atom_object_collection.

        The method return a set of Object filled with atoms data.
        """
        if not self.__atom_object_collection:
            mapper = DatalogMapper.get_instance()
            for atom in self.__atom_string_collection:
                obj = mapper.get_object(atom)
                if obj is not None:
                    self.__atom_object_collection.add(obj)
        return self.__atom_object_collection

    def __str__(self):
        """Overload string method."""
        return str(self.__atom_string_collection)
