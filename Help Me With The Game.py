lst = list()
while True:
    line = input()
    if line[0] == '+':
        continue
    else:
        lst.append(line[2::4])
    if len(lst) == 8:
        break
# print(lst)
# =========================== black and white division
white, black = list(), list()
column = 'abcdefgh'
for row in range(len(lst)):
    for j in range(len(lst[row])):
        element = lst[row][j]
        if element.isalpha():
            if element.isupper():
                white.append(element + column[j] + str(8 - row))
            else:
                black.append(element.upper() + column[j] + str(8 - row))


# ============================ ordering function for lists


def ordering(colorList):
    k, q, r, b, n, p = [], [], [], [], [], []

    while len(colorList) != 0:
        if 'K' == colorList[0][0]:
            k.append(colorList[0])
        elif 'Q' == colorList[0][0]:
            q.append(colorList[0])
        elif 'R' == colorList[0][0]:
            r.append(colorList[0])
        elif 'B' == colorList[0][0]:
            b.append(colorList[0])
        elif 'N' == colorList[0][0]:
            n.append(colorList[0])
        else:
            p.append(colorList[0].replace('P', ''))
            p.sort(key=lambda p: p[1], reverse=True)
        colorList.pop(0)
    answer = k + q + r + b + n + p
    return answer
    # return *k, *q


# ================================== output
print('White: ', end='')
print(*ordering(white), sep=',')
print('Black: ', end='')
print(*ordering(black), sep=',')
# =========================================================
# =========================================================

table = []
for i in range(8):
    input()
    table += [list(map(lambda x: x[1:-1], input().split('|')[1:-1]))]
input()
table.reverse()
print(table)
# =====

pieces = {'K': [], 'Q': [], 'R': [], 'B': [], 'N': [], 'P': [], 'k': [], 'q': [], 'r': [], 'b': [], 'n': [], 'p': []}

for i in range(8):
    for j in range(8):
        if table[i][j] in pieces.keys():
            pieces[table[i][j]] += [((lambda c: c.upper() if c.lower() != 'p' else '')(table[i][j]), chr(97+j), i + 1)]

print(pieces)
for key, val in pieces.items():
    if key.isupper():
        val.sort(key=lambda x: (x[2], x[1]))
    else:
        val.sort(key=lambda x: (-x[2], x[1]))
print(pieces)

print('White: ', end='')
print(','.join(list(map(lambda x: (x[0]+x[1]+str(x[2])), (pieces['K'] + pieces['Q'] + pieces['R'] + pieces['B'] + pieces['N'] + pieces['P'])))))
print('Black: ', end='')
print(','.join(list(map(lambda x: (x[0]+x[1]+str(x[2])), (pieces['k'] + pieces['q'] + pieces['r'] + pieces['b'] + pieces['n'] + pieces['p'])))))


'''
White: Ke1,Qd1,Ra1,Rh1,Bc1,Bf1,Nb1,e4,a3,a2,c2,d2,f2,g2,h2
Black: Ke8,Qd8,Ra8,Rh8,Bc8,Ng8,Nc6,a7,b7,c7,d7,e7,f7,h7,h6'''