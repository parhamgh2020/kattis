exist = kings, queens, rooks, bishops, knights, pawns = list(map(int,input().split()))
right = (1, 1, 2, 2, 2, 8)
for i in range(len(exist)):
    print(right[i] - exist[i], end=' ')
