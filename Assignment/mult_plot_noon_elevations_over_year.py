import math
import numpy as np
import matplotlib.pyplot as plt
from datetime import date, timedelta


def nice_date_str(day_num):
    day_num = int(day_num)
    base_date = date(2022, 1, 1)
    delta = timedelta(days=day_num)
    the_date = base_date + delta
    return the_date.strftime("%d, %b")


def solar_declination(day_num, solar_hour):
    n = day_num + solar_hour / 24
    beta = 360 / 365 * (n + 10)
    return -23.44 * cos_d(beta)


def solar_hour_angle(solar_hour):
    return 15 * (solar_hour - 12)


def solar_elevation(latitude, day_num, solar_hour):
    hour_angle = solar_hour_angle(solar_hour)
    declination = solar_declination(day_num, solar_hour)
    elevation = asin_d(sin_d(latitude) * sin_d(declination) + cos_d(latitude) * cos_d(declination) * cos_d(hour_angle))
    return elevation


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


def multi_plot_noon_elevations_over_year(latitude):
    counter = 0
    while len(latitude) != counter:
        elevations = solar_elevation(latitude[counter], np.arange(0, 364), 12)
        plt.plot(np.arange(0, 364), elevations, linestyle="-")
        counter = counter + 1
    plt.xticks(np.arange(0, 360 + 1, 30))
    plt.yticks(np.arange(-90, 90 + 1, 10))
    plt.xlabel("day")
    plt.ylabel("noon Solar Elevation (degrees)")
    plt.grid()
    plt.show()


multi_plot_noon_elevations_over_year([-90, -60, -30, 0])
