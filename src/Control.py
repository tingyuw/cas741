# \file Control.py
# \brief Controls the flow of the program
import sys
import time
import coverage

import Calculations
import InputConstraints
import InputParameters
import OutputFormat

# start timer
start = time.time()

# start coverage
cov = coverage.Coverage()
cov.start()

filename = sys.argv[1]
f = open(filename, "r")
# read input
(F_1, X_1, X_2, theta_1, theta_2) = InputParameters.get_input(f)
f.close()
inParams = (F_1, X_1, X_2, theta_1, theta_2)
calledfunc = "Control"

# do the calculationsif inputs are valid
if (InputConstraints.input_constraints(inParams, calledfunc)):
    (F_Ax, F_Ay, F_By) = InputParameters.derived_values(F_1, X_1, X_2)
    F_AC = Calculations.func_F_AC(F_Ay, theta_1)
    F_AD = Calculations.func_F_AD(F_AC, theta_1)
    F_BC = Calculations.func_F_BC(F_By, theta_2)
    F_BD = Calculations.func_F_BD(F_BC, theta_2)
    F_CD = Calculations.func_F_CD(F_1)
    OutputFormat.write_output(F_AC, F_AD, F_BC, F_BD, F_CD)

cov.stop()
cov.save()

# generate coverage report
cov.html_report()

# end timer
end = time.time()
print("execution time = ", end - start)
