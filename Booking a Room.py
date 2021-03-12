import random

r, n = map(int, input().split())
rooms = [x for x in range(1, r + 1)]
for i in range(n):
    rooms.remove(int(input()))

if n == r:
    print('too late')
else:
    print(random.choice(rooms))
