h, m = list(map(int, input().split()))
if (h * 60 + m - 45) > 60:
    H = (h * 60 + m - 45) // 60
    M = (h * 60 + m - 45) % 60
else:
    H = 23
    M = 60 - (45 - m)

print(H, M)

# lst = []
# for _ in range(0, 24):
#     lst.append(60)
#
# lst[h] + m - 45
