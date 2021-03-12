while True:
    a, b = ini = tuple(map(int, input().split()))
    if ini == (0, 0):
        break
    elif sum(ini) == 13:
        print('Never speak again.')
    elif a > b:
        print('To the convention.')
    elif a < b:
        print('Left beehind.')
    elif a == b:
        print('Undecided.')
