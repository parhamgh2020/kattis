n, w, h = list(map(int, input().split()))

for _ in range(n):
    if int(input()) <= (w ** 2 + h ** 2) ** 0.5:
        print('DA')
    else:
        print('NE')
