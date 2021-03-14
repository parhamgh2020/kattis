n, c = map(int, input().split())
lst = list(map(int, input().split()))

max_belly = -1
for i in range(n):
    belly = []
    for j in lst[i:]:
        next_fruit = j
        check = sum(belly) + next_fruit
        if check > c:
            continue
        else:
            belly.append(next_fruit)
    max_belly = max(max_belly, len(belly))
print(max_belly)
