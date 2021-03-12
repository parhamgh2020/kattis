inp_ = list()
code = [str(i) for i in range(1, 10)]
location = list()
for _ in range(3):
    inp_.append(input().split())
    # inp_.append(list(enumerate(input().split())))
# print(inp_)
for code in code:
    for x in range(len(inp_)):
        if code in inp_[x]:
            location.append((x, inp_[x].index(code)))
length = 0
for i in range(1, len(location)):
    length += ((location[i][0] - location[i - 1][0]) ** 2 + (location[i][1] - location[i - 1][1]) ** 2) ** 0.5

print(length)
