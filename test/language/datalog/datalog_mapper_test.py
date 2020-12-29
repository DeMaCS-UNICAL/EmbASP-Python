import unittest

from embasp.languages.datalog.datalog_mapper import DatalogMapper

from ..asp.cell import Cell
from .arity0 import Arity0


class DatalogMapperTest(unittest.TestCase):

    def runTest(self):

        instance = DatalogMapper.get_instance()

        try:
            instance.register_class(Cell)

            obj = instance.get_object("cell(2,4,6)")

            self.assertTrue(isinstance(obj, Cell))

            self.assertEqual(2, obj.get_row())

            self.assertEqual(4, obj.get_column())

            self.assertEqual('6', obj.get_value().value)

            self.assertEqual("cell(2,4,6)", instance.get_string(obj))

            instance.unregister_class(Cell)

            noneObject = instance.get_object("cell(2,4,6)")

            self.assertIsNone(noneObject)

            instance.register_class(Arity0)

            zeroArityObject = instance.get_object("a")

            self.assertIsNotNone(zeroArityObject)

            self.assertTrue(isinstance(zeroArityObject, Arity0))

            self.assertEqual("a()", instance.get_string(zeroArityObject))

        except Exception as e:
            self.fail(str(e))


if __name__ == '__main__':
    unittest.main()
