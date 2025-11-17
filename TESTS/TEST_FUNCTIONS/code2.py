import math
import random

def square(x):
    return x * x

def random_between(a, b):
    return random.randint(a, b)

def circle_area(radius):
    return math.pi * square(radius)
