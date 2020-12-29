import os
import sys
import unittest

from embasp.base.output import Output
from embasp.languages.asp.asp_input_program import ASPInputProgram
from embasp.platforms.desktop.desktop_handler import DesktopHandler
from embasp.specializations.clingo.desktop.clingo_desktop_service import \
    ClingoDesktopService

from .cell import Cell
from .my_callback import MyCallback


class ClingoDesktopServiceTest(unittest.TestCase):

    n = 9
    inputMatrix = [[1, 0, 0, 0, 0, 7, 0, 9, 0],
                   [0, 3, 0, 0, 2, 0, 0, 0, 8],
                   [0, 0, 9, 6, 0, 0, 5, 0, 0],
                   [0, 0, 5, 3, 0, 0, 9, 0, 0],
                   [0, 1, 0, 0, 8, 0, 0, 0, 2],
                   [6, 0, 0, 0, 0, 4, 0, 0, 0],
                   [3, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 4, 1, 0, 0, 0, 0, 0, 7],
                   [0, 0, 7, 0, 0, 0, 3, 0, 0]]

    def getPath(self):
        OS = sys.platform
        path = os.path.join("test-resources", "asp", "executables", "clingo")
        if OS.startswith("win32"):
            if sys.maxsize > 2**32:
                path = os.path.join(path, "clingo64.exe")
            else:
                path = os.path.join(path, "clingo32.exe")
        else:
            if OS.startswith("darwin"):
                path = os.path.join(path, "clingo_macos")
            else:
                if OS.startswith("linux"):
                    path = os.path.join(path, "clingo_linux")

        return path

    def test_sudoku(self):
        try:
            handler = DesktopHandler(ClingoDesktopService(self.getPath()))

            inp = ASPInputProgram()

            for i in range(9):
                for j in range(9):
                    if (self.inputMatrix[i][j] != 0):
                        inp.add_object_input(
                            Cell(i, j, self.inputMatrix[i][j]))

            inp.add_files_path(os.path.join("test-resources", "asp", "sudoku"))

            handler.add_program(inp)

            mc = MyCallback()

            handler.start_async(mc)

            mc.wait_the_end()

            out = mc.get_output()

            # out = handler.startSync()

            self.assertIsNotNone(out)
            self.assertTrue(isinstance(out, Output),
                            "Error, result object is not Output")
            self.assertTrue(out.get_errors() == "",
                            "Found error:\n" + str(out.get_errors()))
            self.assertTrue(len(out.get_answer_sets()) != 0)

            ans = out.get_answer_sets()[0]

            for obj in ans.get_atoms():
                self.inputMatrix[obj.get_row()][obj.get_column()
                                                ] = obj.get_value()

            tmp = ""
            for i in range(9):
                for j in range(9):
                    tmp += str(self.inputMatrix[i][j]) + " "
                print(tmp)
                tmp = ""

        except Exception as e:
            self.fail("Exception " + str(e))


if __name__ == '__main__':
    unittest.main()
