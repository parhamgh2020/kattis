
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a, " ", int(b * (b + 1) / 2 + b))
