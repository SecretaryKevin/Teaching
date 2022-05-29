import math
import numpy as np
import matplotlib.pyplot as plt


def cos_d(degrees):
    """ To save us converting to radians all the time """
    return np.cos(np.radians(degrees))


def sin_d(degrees):
    """ To save us converting to radians all the time """
    return np.sin(np.radians(degrees))


def asin_d(n):
    """ Returns the degrees such that sin(degrees) == n
    This is also know as the inverse sin function or arcsin.
    The stanard asin function returns the value in radians.
    This function converts the result to degrees
    """
    return np.degrees(np.arcsin(n))


values = np.array([0, 30, 60, 90])
cozes = cos_d(values)
np.set_printoptions(precision=2, suppress=True)
print(cozes)

