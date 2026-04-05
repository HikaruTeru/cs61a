

from math import sqrt, pi

def area_square(r):
    assert r > 0, 'A length must be positive'
    return r * r

def area_circle(r):
    assert r > 0, 'A length must be positive'
    return r * r * pi

def area_hexagon(r):
    assert r > 0, 'A length must be positive'
    return r * r * 3 * sqrt(3) / 2



