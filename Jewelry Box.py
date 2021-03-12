for _ in range(int(input())):
    x, y = map(int, input().split())
    max_vol = int()
    for a in range(x):
        for b in range(y):
            for h in range(max(x, y) - max(a, b)):
                if a + h == x:
                    if b + h == y:
                        if a * b * h > max_vol:
                            max_vol = a * b * h
    print(max_vol)
