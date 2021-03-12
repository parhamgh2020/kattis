keys = " ‘ 1 2 3 4 5 6 7 8 9 0 - = q w e r t y u i o p [ ] \ a s d f g h j k l ; ' z x c v b n m , . / ".upper().split()
while (True):
    out = list()
    try:
        line = input()
    except EOFError:
        break
    for i in line:
        if i == ' ':
            out.append(' ')
        else:
            out.append(keys[keys.index(i) - 1])
    print(''.join(out))
