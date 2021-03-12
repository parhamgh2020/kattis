l, h = input().split()
lst = list()
for num in range(int(l), int(h) + 1):
    for i in str(num):
        if str(num).count(i) != 1:
            break
        if int(i) == 0:
            break
        if int(num) % int(i) != 0:
            break
    else:
        lst.append(num)

print(len(lst))
