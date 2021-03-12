inp = input().split()
answer = list()
for i in inp:
    answer.append(int(i[::-1]))

answer = max(answer)
print(answer)