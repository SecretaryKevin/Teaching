import numpy as np


def times_across_day(days):
    """"Returns a numpy array of evenly spaced times between 0 and 24 inclusive"""
    return np.linspace(0, 24, days)


values = times_across_day(3)
np.set_printoptions(precision=2, suppress=True)
print(values)

values = times_across_day(5)
np.set_printoptions(precision=2, suppress=True)
print(values)
