import os
import sys
from datetime import datetime, timedelta
from math import pi, sqrt

import module_1
import numpy as np


def calculate_circle_area(radius):
    return pi * radius**2


a = [
    1,
    2,
    3,
    4,
    5,
]


def some_long_function(argument_1, argument_2, argument_3, argument_4, argument_5, *args, **kwargs):
    pass


def main():
    radius = 5
    area = calculate_circle_area(radius)
    print(f"The area of a circle with radius {radius} is: {area}")
    today = datetime.now()
    print(f"Today is {today.strftime('%Y-%m-%d')}")

    print('"ffff')

    delta = timedelta(days=5)
    future_date = today + delta
    print(f"In 5 days, it will be: {future_date.strftime('%Y-%m-%d')}")


main()
