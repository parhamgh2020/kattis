from math import pi

while True:
    r, m, c = map(float, input().split())
    if r == m == c == 0:
        break
    square_area = 2 * r * 2 * r
    circle_area = pi * r ** 2
    estimate = c / m * square_area
    print(circle_area, estimate)
