import unittest
import coverage

import InputParameters
import Calculations

cov = coverage.Coverage()
cov.start()


def relerr(actual, expected):
    return abs(actual - expected)/expected


# Test module Calculations #
class OutputCorrectnessTest(unittest.TestCase):
    def test_output(self):
        (F_1, X_1, X_2, theta_1, theta_2) = (500, 3, 3, 45, 45)
        (F_Ax, F_Ay, F_By) = InputParameters.derived_values(F_1, X_1, X_2)
        F_AC = Calculations.func_F_AC(F_Ay, theta_1)
        F_AD = Calculations.func_F_AD(F_AC, theta_1)
        F_BC = Calculations.func_F_BC(F_By, theta_2)
        F_BD = Calculations.func_F_BD(F_BC, theta_2)
        F_CD = Calculations.func_F_CD(F_1)
        assert relerr(F_AC, -353.553) < 0.01
        assert relerr(F_AD, 250) < 0.01
        assert relerr(F_BC, -353.553) < 0.01
        assert relerr(F_BD, 250) < 0.01
        assert relerr(F_CD, 500) < 0.01


if __name__ == "__main__":
    unittest.main(verbosity=2)

cov.stop()
cov.save()

cov.html_report()
