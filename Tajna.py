def rc(inp):
    l = len(inp)
    i = 1
    while (i <= l / i):
        if l % i == 0 and i <= (l / i):
            r = i
            c = l // i
        i += 1
    return r, c


inp = input()
r, c = rc(inp)
for i in range(r):
    for j in range(c):
        print(inp[i + (j * r)], end='')
