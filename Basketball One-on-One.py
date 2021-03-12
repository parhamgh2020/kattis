ini = input()
A, B = int(), int()
for i in range(len(ini)):
    if ini[i] == 'A':
        A += int(ini[i + 1])
    elif ini[i] == 'B':
        B += int(ini[i + 1])
    else:
        None
print('A' if A > B else 'B')
