x_point = list()
y_point = list()
answer = list()

for _ in range(3):
    x, y = list(map(int, input().split()))
    x_point.append(x)
    y_point.append(y)

for i in x_point:
    if x_point.count(i) == 1:
        answer.append(i)
for i in y_point:
    if y_point.count(i) == 1:
        answer.append(i)

print(answer[0], answer[1])
