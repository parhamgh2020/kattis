n = int(input())
mat = list()
answer = float()
for i in range(n):
    mat.append(list(map(float, input().split())))
for i in range(n - 1):
    a = (mat[i + 1][0] - mat[i][0])
    b = (mat[i][1] + mat[i + 1][1]) / 2
    answer += a * b
print(answer * 10 ** -3)
