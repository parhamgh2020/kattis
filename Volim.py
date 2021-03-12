# 3 minutes and 30 seconds
num_p = int(input())
players = int(input())
time = 3 * 60 + 30
while True:
    t, a = input().split()
    time -= int(t)
    if time <= 0:
        break
    if a == 'T':
        if num_p == 8:
            num_p = 1
        else:
            num_p += 1
print(num_p)
