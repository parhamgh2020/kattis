import fileinput

for line in fileinput.input():
    lst = list(map(int, line.split()))
    print(sum(lst) // 2)

