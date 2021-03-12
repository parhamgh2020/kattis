a, b = 0, 0
for _ in range(int(input())):
    i, j = map(int, input().split())
    a += i * 60
    b += j
print(format(b / a, '.9f') if b / a > 1 else 'measurement error')
