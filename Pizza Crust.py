from math import pi

r, c = map(int, input().split())
percentage = ((pi * (r - c) ** 2) / (pi * r ** 2)) * 100
print(percentage)
