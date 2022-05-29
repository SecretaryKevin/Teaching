import math
import numpy as np
import matplotlib.pyplot as plt
from datetime import date, timedelta


def nice_date_str(day_num):
    """
    Return a nice string representation of a day number
    :param day_num: number of days since the start of the year
    :return:
    """
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


def plot_elevation_over_day(latitude, day_num, number_of_points):
    """
    Plot the elevation of the sun over the day
    :param latitude: latitude in degrees
    :param day_num: number of days since the start of the year
    :param number_of_points: number of points to plot
    :return:
    """
    number_of_points = np.linspace(0, 24, number_of_points)
    elevation = solar_elevation(latitude, day_num, number_of_points)
    print(elevation)
    plt.plot(number_of_points, elevation, color='orange', linestyle="", marker="o", markersize=10)
    plt.xticks(np.arange(0, 24 + 1, 1))
    plt.yticks(np.arange(-90, 90 + 1, 10))
    plt.xlabel("Solar Hours")
    plt.ylabel("Solar Elevation (degrees)")
    plt.title(f"Solar elevations for day={nice_date_str(day_num)}, latitude={round(latitude, 2)}")
    plt.grid()
    plt.show()


plot_elevation_over_day(-43.52565, 0, 25)
