lst = list()
for _ in range(5):
    lst.append(input())

counter = int()
for i in range(len(lst)):
    if 'FBI' in lst[i]:
        print(i + 1, end=' ')
        counter += 1
if counter == 0:
    print('HE GOT AWAY!')
