n, m = map(int, input().split())
lst = list()
for _ in range(n):
    lst.append(' '.join(input()).split())


def func(ls, x, y):
    ls[x][y] = 'V'
    if x < len(lst) - 1:
        if ls[x + 1][y] != '#':
            return func(ls, x + 1, y)
        else:
            if len(ls[x]) - 1 > y > 0:
                if ls[x][y + 1] == '.' and ls[x][y - 1] == '.':
                    return func(ls, x, y + 1), func(ls, x, y - 1)
            if y > 0:
                if ls[x][y - 1] == '.':
                    return func(ls, x, y - 1)
            if y < len(ls[x]) - 1:
                if ls[x][y + 1] == '.':
                    return func(ls, x, y + 1)


for i in range(n):
    for j in range(m):
        if lst[i][j] == 'V':
            func(lst, i, j)
for i in range(len(lst)):
    print(*lst[i], sep='')
