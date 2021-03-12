answer = str()
for i in range(int(input())):
    in__ = input()
    if 'Simon says ' in in__:
        in__ = in__.replace('Simon says ', '')
        answer += in__ + '\n'

print(answer)
