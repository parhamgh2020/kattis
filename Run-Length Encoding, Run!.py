code, inp = input().split()
answer = str()
if code == 'E':
    letter = ''
    count = 0
    for i in range(len(inp)):
        if inp[i] == letter:
            count += 1
        else:
            if letter:
                answer += letter + str(count)
            count = 1
            letter = inp[i]
    answer += inp[-1] + str(count)
elif code == 'D':
    for i in range(len(inp)):
        if not inp[i].isdigit():
            answer += inp[i] * int(inp[i + 1])

print(answer)
