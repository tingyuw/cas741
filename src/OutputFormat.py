# \file OutputFormat.py
# \brief Provides the function for writing outputs
# \brief Writes the output values to output.txt

def write_output(F_AC, F_AD, F_BC, F_BD, F_CD):
    outputfile = open("output.txt", "w")
    # print F_AC
    print("F_AC = ", end="", file=outputfile)
    print(abs(round(F_AC, 3)), end="", file=outputfile)
    print("N, and it is in ", end="", file=outputfile)
    if F_AC > 0:
        print("tension.", file=outputfile)
    elif F_AC < 0:
        print("compression.", file=outputfile)
    # print F_AD
    print("F_AD = ", end="", file=outputfile)
    print(abs(round(F_AD, 3)), end="", file=outputfile)
    print("N, and it is in ", end="", file=outputfile)
    if F_AD > 0:
        print("tension.", file=outputfile)
    elif F_AD < 0:
        print("compression.", file=outputfile)
    # pring F_BC
    print("F_BC = ", end="", file=outputfile)
    print(abs(round(F_BC, 3)), end="", file=outputfile)
    print("N, and it is in ", end="", file=outputfile)
    if F_BC > 0:
        print("tension.", file=outputfile)
    elif F_BC < 0:
        print("compression.", file=outputfile)
    # print F_BD
    print("F_BD = ", end="", file=outputfile)
    print(abs(round(F_BD, 3)), end="", file=outputfile)
    print("N, and it is in ", end="", file=outputfile)
    if F_BD > 0:
        print("tension.", file=outputfile)
    elif F_BD < 0:
        print("compression.", file=outputfile)
    # print F_CD
    print("F_CD = ", end="", file=outputfile)
    print(abs(round(F_CD, 3)), end="", file=outputfile)
    print("N, and it is in ", end="", file=outputfile)
    if F_CD > 0:
        print("tension.", file=outputfile)
    elif F_CD < 0:
        print("compression.", file=outputfile)

    outputfile.close()
