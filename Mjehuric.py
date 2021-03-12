a = list(map(int, input().split()))
while True:
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            print(*a)

    for i in range(len(a)):
        if max(a[0:i + 1]) == a[i]:
            continue
        else:
            break
    else:
        break

