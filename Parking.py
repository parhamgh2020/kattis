# import statistics

for _ in range(int(input())):
    input()
    lst = list(map(int, input().split()))
    # to_last = max(lst) - statistics.mean(lst)
    # to_first = statistics.mean(lst) - min(lst)
    distance = (max(lst) - min(lst)) * 2
    print(distance)

