rectangles = list()
circles = list()
for _ in range(int(input())):
    inp = input().split()
    if inp[0] == 'rectangle':
        rectangles.append([int(inp[i]) for i in range(1, len(inp))])
    else:
        circles.append([int(inp[i]) for i in range(1, len(inp))])
# print(rectangles)
# print(circles)
shots = list()
for _ in range(int(input())):
    shots.append(list(map(int, input().split())))


def rec_shot(s, rec):
    if rec[0] <= s[0] <= rec[2] and rec[1] <= s[1] <= rec[3]:
        return True
    else:
        return False


def cir_shot(s, cir):
    if ((s[0] - cir[0]) ** 2 + (s[1] - cir[1]) ** 2) ** 0.5 <= cir[2]:
        return True
    else:
        return False


result = list()
for i in shots:
    r = int()
    for j in rectangles:
        if rec_shot(i, j):
            r += 1
    for j in circles:
        if cir_shot(i, j):
            r += 1
    result.append(r)

print(*result, sep='\n')
