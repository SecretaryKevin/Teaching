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


def mult_plot_elevations_over_days(latitude, day_num, number_of_points):
    counter = 0
    elevations = []
    number_of_points = np.linspace(0, 24, number_of_points)
    while len(day_num) != counter:
        elevations.append(solar_elevation(latitude, day_num[counter], number_of_points))
        plt.plot(number_of_points, elevations[counter], label=f"{nice_date_str(day_num[counter])}", linestyle="-",
                 marker=None, )
        counter = counter + 1
    """start of the plot"""
    plt.xticks(np.arange(0, 24 + 1, 1))
    plt.yticks(np.arange(-90, 90 + 1, 10))
    plt.xlabel("Solar Hours")
    plt.ylabel("Solar Elevation (degrees)")
    plt.title(f"Solar elevations for latitude={round(latitude, 2)}")
    plt.legend()

    plt.grid()
    plt.show()


mult_plot_elevations_over_days(-43.525650, [0, 90, 180, 270], 25)
