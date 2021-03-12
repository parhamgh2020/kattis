def my_func(a):
    lst = [[0, 0]]
    for _ in range(a):
        lst.append(input().split())

    # print(lst)
    miles = 0
    for i in range(1, a + 1):
        # miles += int(lst[i][0]) * (int(lst[i][0]) - int(lst[i - 1][1]))
        x = int(lst[i][0])
        y = int(lst[i][1])
        z = int(lst[i - 1][1])
        miles += x * (y - z)
    return miles


answer = list()
while True:
    a = int(input())
    if a > 0:
        answer.append(my_func(a))
    else:
        for i in range(len(answer)):
            print(answer[i], "miles")
        break
