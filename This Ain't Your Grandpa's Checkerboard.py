lst = list()
for _ in range(int(input())):
    lst.append(input())


def check(lst):
    for r in lst:
        if r.count('W') != r.count('B'):
            return False
        w, b = 0, 0
        for c in r:
            if c == 'W':
                w += 1
                b = 0
            else:
                b += 1
                w = 0
            if w > 2 or b > 2:
                return False
    return True


def rev(lst):
    rev = list()
    for c in range(len(lst[0])):
        row = list()
        for r in range(len(lst)):
            row.append(lst[r][c])
        rev.append(row)
    return rev


print(int(check(lst) and check(rev(lst))))
