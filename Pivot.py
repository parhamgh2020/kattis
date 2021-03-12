# n = int(input())
# lst = list(map(int, input().split()))
#
#
# def is_pivot(lst, pivot_index, n):
#     pivot = lst[pivot_index]
#     for j in range(0, pivot_index):
#         if lst[j] > pivot:
#             return False
#     for k in range(pivot_index + 1, n):
#         if lst[k] < pivot:
#             return False
#     return True
#
#
# counter = 0
# for i in range(n):
#     if is_pivot(lst, i, n):
#         counter += 1
# print(counter)

from collections import  deque

n = int(input())
lst = list(map(int, input().split()))

p_list = list()
max_ = 0
for item in lst:
    if item > max_:
        p_list.append(item)
        max_ = item
    else:
        for i in p_list[::-1]:
            if i > item:
                p_list.pop(p_list.index(i))
            else:
                break
print(len(p_list))