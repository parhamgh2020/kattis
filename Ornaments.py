from math import sqrt, acos, pi


def length(r, h, s):
    knot_to_circle = sqrt(h ** 2 - r ** 2) * 2
    angle = pi / 2 - acos(r / h)
    half_circle = pi * r
    circle_plus = (angle * r) * 2
    return (knot_to_circle + half_circle + circle_plus) * (1 + s / 100)


def main():
    while True:
        r, h, s = map(int, input().split())
        if r == h == s == 0:
            break
        print('%.2f' % length(r, h, s))


if __name__ == '__main__':
    main()
