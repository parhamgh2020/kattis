a = int(input())
b = input()
b = b.split()
counter = 0
for i in b:
    i = int(i)
    if i < 0:
        counter += 1

print(counter)
