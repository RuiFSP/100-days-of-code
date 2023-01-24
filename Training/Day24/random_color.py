from random import randint


def create_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb_color = (r, g, b)

    return rgb_color
