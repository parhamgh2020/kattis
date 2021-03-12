r, c = map(int, input().split())
parking_map = list()
for r in range(r):
    parking_map.append(input())

squash_group = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
for i in range(len(parking_map) - 1):
    for j in range(len(parking_map[i]) - 1):
        if '#' not in parking_map[i][j:j + 2] and '#' not in parking_map[i + 1][j:j + 2]:
            squash = parking_map[i][j:j + 2].count('X') + parking_map[i + 1][j:j + 2].count('X')
            squash_group[squash] += 1
for i in squash_group.keys():
    print(squash_group[i])
