for _ in range(int(input())):
    a, b, c = lst = list(map(int, input().split()))
    if a + b == c or a - b == c or a / b == c or a * b == c or b - a == c or b / a == c:
        print('possible')
    else:
        print('impossible')
