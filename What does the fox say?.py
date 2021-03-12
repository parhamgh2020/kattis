for _ in range(int(input())):
    inp1 = input().split()
    while True:
        inp2 = input().split()
        if inp2[0] == 'what':
            break
        for i in range(len(inp1)):
            if inp2[2] == inp1[i]:
                inp1[i] = '_'
    for i in inp1:
        if i != '_':
            print(i, end=' ')