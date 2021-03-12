for case in range(int(input())):
    input()
    ropes = input().split()
    red, blue = list(), list()
    for i in ropes:
        j = int(i.replace(i[-1], ''))
        if 'R' in i:
            red.append(j)
        else:
            blue.append(j)
    length = 0
    for i in range(min(len(red), len(blue))):
        length += red.pop(red.index(max(red)))
        length += blue.pop((blue.index(max(blue))))
        length -= 2
    print(f'Case #{case + 1}:', end=' ')
    print(length)

