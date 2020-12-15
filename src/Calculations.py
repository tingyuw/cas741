import math


def func_F_AC(F_Ay, theta_1):
    return -F_Ay / math.sin(math.radians(theta_1))


def func_F_AD(F_AC, theta_1):
    return -F_AC * math.cos(math.radians(theta_1))


def func_F_BC(F_By, theta_2):
    return -F_By / math.sin(math.radians(theta_2))


def func_F_BD(F_BC, theta_2):
    return -F_BC * math.cos(math.radians(theta_2))


def func_F_CD(F_1):
    return F_1
