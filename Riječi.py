n = int(input())
s = 'A'
for i in range(1, n + 1):
    if i == 1:
        s = s.replace('A', 'B')
    elif i == 2:
        s += 'A'
    elif s[-1] == 'A':
        s += 'B'
    elif s[-1] == 'B' and s[-2] == 'B':
        s += 'A'
    else:
        s += 'B'

print(s.count('A'), s.count('B'))