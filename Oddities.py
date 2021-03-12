lst = list()
for _ in range(int(input())):
    lst.append(int(input()))

for i in lst:
    print(i, 'is', 'even' if i % 2 == 0 else 'odd')
