p, n = map(int, input().split())
part_list = set()
for i in range(1, n + 1):
    part_list.add(input())
    if len(part_list) == p:
        print(i)
        break
else:
    print('paradox avoided')

