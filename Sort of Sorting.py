while True:
    seq = int(input())
    if seq == 0:
        break
    lst = list()
    for _ in range(seq):
        lst.append(input())
    lst.sort(key=lambda l : l[0:2])
    print(*lst, sep='\n')
    print()
