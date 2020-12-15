import Constants


def input_constraints(inParams, calledfunc):
    F_1 = inParams[0]
    X_1 = inParams[1]
    X_2 = inParams[2]
    theta_1 = inParams[3]
    theta_2 = inParams[4]

    if (not(Constants.Constants.F_min <= F_1 and F_1 <= Constants.Constants.F_max)):
        if(calledfunc == "Control"):
            print("Warning: ", end="")
            print("F_1 has value ", end="")
            print(F_1, end="")
            print(", but it is suggested to be ", end="")
            print("between ", end="")
            print(Constants.Constants.F_min, end="")
            print(" and ", end="")
            print(Constants.Constants.F_max, end="")
            print(".")
            return False
        else:
            return False

    if (not(Constants.Constants.d_min < X_1 and X_1 <= Constants.Constants.d_max)):
        if(calledfunc == "Control"):
            print("Warning: ", end="")
            print("X_1 has value ", end="")
            print(X_1, end="")
            print(", but it is suggested to be ", end="")
            print("between ", end="")
            print(Constants.Constants.d_min, end="")
            print(" (not included)", end="")
            print(" and ", end="")
            print(Constants.Constants.d_max, end="")
            print(".")
            return False
        else:
            return False

    if (not(Constants.Constants.d_min < X_2 and X_2 <= Constants.Constants.d_max)):
        if(calledfunc == "Control"):
            print("Warning: ", end="")
            print("X_2 has value ", end="")
            print(X_2, end="")
            print(", but it is suggested to be ", end="")
            print("between ", end="")
            print(Constants.Constants.d_min, end="")
            print(" (not included)", end="")
            print(" and ", end="")
            print(Constants.Constants.d_max, end="")
            print(".")
            return False
        else:
            return False

    if (not(Constants.Constants.theta_min < theta_1 and theta_1 < Constants.Constants.theta_max)):
        if(calledfunc == "Control"):
            print("Warning: ", end="")
            print("theta_1 has value ", end="")
            print(theta_1, end="")
            print(", but it is suggested to be ", end="")
            print("greater than ", end="")
            print(Constants.Constants.theta_min, end="")
            print(" and less than ", end="")
            print(Constants.Constants.theta_max, end="")
            print(".")
            return False
        else:
            return False

    if (not(Constants.Constants.theta_min < theta_2 and theta_2 < Constants.Constants.theta_max)):
        if(calledfunc == "Control"):
            print("Warning: ", end="")
            print("theta_2 has value ", end="")
            print(theta_2, end="")
            print(", but it is suggested to be ", end="")
            print("greater than ", end="")
            print(Constants.Constants.theta_min, end="")
            print(" and less than ", end="")
            print(Constants.Constants.theta_max, end="")
            print(".")
            return False
        else:
            return False

    return True
