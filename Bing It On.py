n = int(input())
lst = []
for _ in range(n):
    inp = input()
    counter = 0
    for word in lst:
        if word.startswith(inp):
            counter += 1
    lst.append(inp)
    print(counter)
