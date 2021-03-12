lst = list()
for i in range(int(input())):
    lst.append(list(map(int, input().split())))
for i in range(len(lst)):
    answer = int()
    for j in range(len(lst[i]) - 2):
        if lst[i][j + 1] > 2 * lst[i][j]:
            answer += lst[i][j + 1] - lst[i][j] * 2
    print(answer)

