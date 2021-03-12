for _ in range(int(input())):
    lst = []
    for _ in range(int(input())):
        lst.append(int(input()))
    ind = lst.index(max(lst))
    if lst.count(max(lst)) > 1:
        print('no winner')
    elif max(lst) > sum(lst) / 2:
        print(f'majority winner {ind + 1}')
    else:
        print(f'minority winner {ind + 1}')
