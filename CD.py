# import datetime
from sys import stdin, stdout

while True:
    mn = stdin.readline().split()
    # a = datetime.datetime.now()
    n, m = map(int, mn)
    a = datetime.datetime.now()
    if n == m == 0:
        # b = datetime.datetime.now()
        # print(b - a)
        break
    jack = set()
    jill = set()
    jill = set(stdin.readline() for _ in range(n))
    jack = set(stdin.readline() for _ in range(m))
    # print(len(jack & jill))
    stdout.write(str(len(jack & jill)) + '\n')

# import datetime
# a = datetime.datetime.now()
# while(True):
#     inp = input().split()
#     N = int(inp[0])
#     M = int(inp[1])
#     if N==0 and M==0:
#         b = datetime.datetime.now()
#         print(b-a)
#         exit()
#     ncd = []
#     for i in range(N):
#         ncd.append(input())
#     mcd = []
#     for i in range(M):
#         mcd.append(input())
#     n = 0
#     m = 0
#     c = 0
#     while(n<N and m<M):
#         if ncd[n] < mcd[m]:
#             n += 1
#         elif ncd[n] > mcd[m]:
#             m += 1
#         else:
#             n += 1
#             m += 1
#             c +=1
#     print(c)
