import unittest
import coverage

import InputConstraints
import InputParameters

cov = coverage.Coverage()
cov.start()

calledfunc = "test"


# Test module InputParameters #
class InputParametersTest(unittest.TestCase):
    def test_input(self):
        filename = "input.txt"
        f = open(filename, "r")
        inParams = InputParameters.get_input(f)
        f.close()
        assert inParams == (500.0, 3.0, 3.0, 45, 45), "Something wrong in the InputParameters.py"


# Test module InputConstraints #
class InputConstraintsTest(unittest.TestCase):
    def test_user_input(self):
        filename = "input.txt"
        f = open(filename, "r")
        inParams = InputParameters.get_input(f)
        f.close()
        validinput = InputConstraints.input_constraints(inParams, calledfunc)
        self.assertTrue(validinput, "Input parameters are not valid.")

    def test_invalid_force(self):
        filename = "testcase_invalidforce.txt"
        f = open(filename, "r")
        for x in range(2):
            f.readline()
            inParams = InputParameters.get_input(f)
            validinput = InputConstraints.input_constraints(inParams, calledfunc)
            self.assertFalse(validinput, "Force is out of bound. It should be false.")
        f.close()

    def test_invalid_distance(self):
        filename = "testcase_invaliddistance.txt"
        f = open(filename, "r")
        for x in range(6):
            f.readline()
            inParams = InputParameters.get_input(f)
            validinput = InputConstraints.input_constraints(inParams, calledfunc)
            self.assertFalse(validinput, "Distance is out of bound. It should be false.")
        f.close()

    def test_invalid_angle(self):
        filename = "testcase_invalidangle.txt"
        f = open(filename, "r")
        for x in range(6):
            f.readline()
            inParams = InputParameters.get_input(f)
            validinput = InputConstraints.input_constraints(inParams, calledfunc)
            self.assertFalse(validinput, "Angle is out of bound. It should be false.")
        f.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)

cov.stop()
cov.save()

cov.html_report()
