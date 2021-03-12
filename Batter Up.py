a = input()
b = input()
b = b.split()

sum_1 = 0
counter = 0

for i in b:
    i = int(i)
    if i >= 0:
        counter += 1
        sum_1 += i

print(sum_1/counter)
