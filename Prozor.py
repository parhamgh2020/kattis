r, s, k = map(int, input().split())
lst = list()
for _ in range(r):
    lst.append(input())
max_ = int()
first_point = []
for n1 in range(0, r - k + 1):
    for n2 in range(0, s - k + 1):
        counter = int()
        for i in range(n1 + 1, n1 + k - 1):
            counter += lst[i][n2 + 1:n2 + k - 1].count('*')
        if counter > max_:
            max_ = counter
            first_point = [n1, n2]

print(max_)
for a1 in range(len(lst)):
    for a2 in range(len(lst[a1])):
        if a1 != n1:
            print(lst[a1][a2], end='')
        elif (a1 == n1 and a2 == n2) or (a1 == n1 + k and a2 == n2) or (a1 == n1 + k and a2 == n2 + k) or (
                a1 == n1 and a2 == n2 + k):
            print('+', end='')
        elif (a1 == n1) or (a1 == n1 + k):
            print('-', end='')
        else:
            print('|', end='')
    print()
