size = int(input())
mtx = list()
for _ in range(size):
    mtx.append(input())


def pl_loc():
    for i in range(size):
        for j in range(size):
            if mtx[i][j] == 'K':
                return i, j
    return None

moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
def func(mtx,i,j):






