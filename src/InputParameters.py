
def get_input(f):
    f.readline()
    F_1 = float(f.readline())
    f.readline()
    X_1 = float(f.readline())
    f.readline()
    X_2 = float(f.readline())
    f.readline()
    theta_1 = float(f.readline())
    f.readline()
    theta_2 = float(f.readline())

    return F_1, X_1, X_2, theta_1, theta_2


def derived_values(F_1, X_1, X_2):
    F_Ax = 0
    F_Ay = F_1 * X_2 / (X_1 + X_2)
    F_By = F_1 * X_1 / (X_1 + X_2)
    print("F_Ax = " + str(F_Ax))
    print("F_Ay = " + str(F_Ay))
    print("F_By = " + str(F_By))
    return F_Ax, F_Ay, F_By
