ini_ = input()
answer = 1
while True:
    for i in ini_:
        if i != '0':
            answer *= int(i)
    if answer < 10:
        break
    else:
        ini_ = str(answer)
        answer = 1
print(answer)
