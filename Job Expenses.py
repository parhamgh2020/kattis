input()
lst = list(map(int, input().split()))
answer = list()
for i in lst:
    if i < 0:
        answer.append(i * -1)

print(sum(answer))
