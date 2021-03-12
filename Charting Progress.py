import fileinput

lst = list()
s = int()
for line in fileinput.input():
    star = line.count('*')
    s += star
    if line == '\n':
        s = 0
        print()
        continue
    for _ in range(len(line) - s - 1):
        print('.', end='')
    for _ in range(star):
        print('*', end='')
    for _ in range(len(line) - 1 - ((len(line) - s - 1) + star)):
        print('.', end='')
    print()
