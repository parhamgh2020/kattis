alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
    answer = ''
    inp = input()
    if inp == '0':
        break
    shift, string = inp.split()
    string = string[::-1]
    for i in range(len(string)):
        alpha_shift = alpha.index(string[i]) + int(shift)
        if alpha_shift < len(alpha):
            answer += alpha[alpha_shift]
        else:
            answer += alpha[alpha_shift % len(alpha)]
    print(answer)
