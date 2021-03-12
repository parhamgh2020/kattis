'''
(D * D * pi) - (d * d * pi) = v  >>>>
'''
from math import pi

while True:
    D, V = map(int, input().split())
    if D == V == 0:
        break
    d = ((D ** 2 * pi) - V) ** 0.5
    print(d)
