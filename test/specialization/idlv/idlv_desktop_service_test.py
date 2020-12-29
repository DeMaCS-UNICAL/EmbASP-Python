import os
import platform
import sys
import unittest

from embasp.languages.datalog.datalog_input_program import DatalogInputProgram
from embasp.languages.datalog.datalog_mapper import DatalogMapper
from embasp.platforms.desktop.desktop_handler import DesktopHandler
from embasp.specializations.idlv.desktop.idlv_desktop_service import \
    IDLVDesktopService

from .edge import Edge
from .path import Path


def getPath():
    path = os.path.join("test-resources",
                        "datalog", "executables", "idlv")

    if sys.platform.startswith("win32"):
        if platform.machine().endswith('64'):
            path = os.path.join(path, "idlv.win.64")
        else:
            path = os.path.join(path, "idlv.win.32")
    else:
        if sys.platform.startswith("linux"):
            if platform.machine().endswith('64'):
                path = os.path.join(path, "idlv.linux.64")
            else:
                path = os.path.join(path, "idlv.linux.32")
        else:
            if sys.platform.startswith("darwin"):
                path = os.path.join(path, "idlv.mac")
    return path


class IDLVDesktopServiceTest(unittest.TestCase):

    """
    A simple test class calculating the transitive closure of a graph.
    """

    def test_find_reachable_nodes(self):
        try:
            o1 = Edge(1, 2)
            o2 = Edge(2, 3)
            o3 = Edge(2, 4)
            o4 = Edge(3, 5)
            o5 = Edge(5, 6)

            handler = DesktopHandler(IDLVDesktopService(getPath()))
            testInputProgram = DatalogInputProgram()
            testInputProgram.add_program("path(X,Y) :- edge(X,Y).")
            testInputProgram.add_program("path(X,Y) :- path(X,Z), path(Z,Y). ")

            testInputProgram.add_object_input(o1)
            testInputProgram.add_object_input(o2)
            testInputProgram.add_object_input(o3)
            testInputProgram.add_object_input(o4)
            testInputProgram.add_object_input(o5)

            handler.add_program(testInputProgram)
            # handler.add_option(OptionDescriptor("--no-projection=0 "))
            # handler.add_option(OptionDescriptor("--no-decomp "))
            # handler.add_option(OptionDescriptor("--t"))

            DatalogMapper.get_instance().register_class(Path)

            minimalModels = handler.start_sync()
            self.assertIsNotNone(minimalModels)
            self.assertTrue(minimalModels.get_errors() == "",
                            "Found error:\n" + str(minimalModels.get_errors()))
            self.assertTrue(len(minimalModels.get_minimal_models()) == 1)

            for o in minimalModels.get_minimal_models().pop().get_atoms_as_objectset():
                if isinstance(o, Path):
                    print(o.__str__())

        except Exception as e:
            print(str(e))


if __name__ == "__main__":
    unittest.main()
