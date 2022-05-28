import math
import numpy as np
import matplotlib.pyplot as plt


def cos_d(degrees):
    """ To save us converting to radians all the time """
    converted_list = []
    for num in degrees:
        temp = math.cos(math.radians(num))
        temp = round(temp, 2)
        temp = np.format_float_positional(temp, trim=".")
        converted_list.append(temp)
    array_new = np.array(converted_list)
    return array_new


def sin_d(degrees):
    """ To save us converting to radians all the time """
    converted_list = []
    for num in degrees:
        temp = math.sin(math.radians(num))
        temp = round(temp, 2)
        temp = np.format_float_positional(temp, trim=".")
        converted_list.append(temp)
    array_new = np.array(converted_list)
    return array_new


def asin_d(n):
    """ Returns the degrees such that sin(degrees) == n
    This is also know as the inverse sin function or arcsin.
    The stanard asin function returns the value in radians.
    This function converts the result to degrees
    """
    converted_list = []
    for num in n:
        temp = math.degrees(math.asin(num))
        temp = round(temp, 2)
        temp = np.format_float_positional(temp, trim=".")
        converted_list.append(temp)
    array_new = np.array(converted_list)
    return array_new


values = np.array([0, 30, 60, 90])
cozes = cos_d(values)
np.set_printoptions(precision=2, suppress=True)
print(cozes)

