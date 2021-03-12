list_1 = input().split()
for i in list_1:
    if list_1.count(i) > 1:
        print('no')
        break
else:
    print('yes')

# print('no' for i in list_1 if list_1.count(i) > 1 else 'yes')  # error
