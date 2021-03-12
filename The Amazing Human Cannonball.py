# x(t) = v0 * t * cos(deta)
# y(t) = v0 * t * sin(deta) - 0.5 * g * t ** 2
import math

y = list()
for _ in range(int(input())):
    v0, deta, x1, h1, h2 = list(map(float, input().split()))
    g = 9.81
    t = x1 / (v0 * math.cos(math.radians(deta)))
    y.append(v0 * t * math.sin(math.radians(deta)) - (0.5 * g * t ** 2))

for i in y:
    if h1 + 1 < i < h2 - 1:
        print("Safe")
    else:
        print("Not Safe")
