# r, c, zr, zc = lst = list(map(int, input().split()))
# mat = list()
# for _ in range(r):
#     mat.append(input())
#
# for row in range(len(mat)):
#     for i in range(zr):
#         for column in range(len(mat)):
#             print(mat[row][column] * zc, end='')
#         print()
# =====================================================
# params = [int(x) for x in input().split()]
#
# for i in range(params[0]):
#     line = input()
#     for j in line:
#         out = "".join([ x*params[3] for x in line ])
#     for j in range(params[2]):
#         print(out)
# ====================================================
r, c, zr, zc = lst = list(map(int, input().split()))
for _ in range(r):
    line = input()
    for i in range(zr):
        for j in line:
            print(j * zc , end='')
        print()

