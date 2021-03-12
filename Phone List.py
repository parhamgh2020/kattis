from collections import deque
from sys import stdin, stdout


def check():
    n = int(input())
    key = input()
    for _ in range(n - 1):
        inp_ = input()
        if inp_.startswith(key) or key == inp_:
            print('NO')
            break
    else:
        print('YES')


for _ in range(int(input())):
    check()

#
#
# def case(amount):
#     numbers = []
#     for _ in range(amount):
#         numbers.append(input())
#
#     numbers.sort()
#     for i in range(len(numbers)):
#         c = numbers[i]
#         for j in range(i + 1, len(numbers)):
#             if numbers[j].startswith(c):
#                 return "NO"
#
#             break
#
#     return "YES"
#
#
# t = int(input())
# for _ in range(t):
#     n = int(input())
# print(case(n))
