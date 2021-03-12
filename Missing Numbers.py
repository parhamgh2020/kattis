lst = list()
miss_lst = list()
for _ in range(int(input())):
    lst.append(int(input()))
i, j = 1, 1
while i < lst[-1]:
    if i < lst[j - 1]:
        miss_lst.append(i)
    else:
        j += 1
    i += 1

if len(miss_lst) == 0:
    print('good job')
else:
    for i in miss_lst:
        print(i)
