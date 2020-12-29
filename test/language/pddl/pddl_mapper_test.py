import unittest
from .pick_up import PickUp

from embasp.languages.pddl.pddl_mapper import PDDLMapper


class PDDLMapperTest(unittest.TestCase):

    def test(self):

        instance = PDDLMapper.get_instance()

        try:
            instance.register_class(PickUp)

            obj = instance.get_object("(pick-up b)")

            self.assertTrue(isinstance(obj, PickUp))

            self.assertEqual("b", obj.get_block())

        except Exception as e:
            self.fail(str(e))


if __name__ == '__main__':
    unittest.main()
