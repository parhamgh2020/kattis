for _ in range(int(input())):
    inp = input()
    if '+' in inp:
        a, b = map(int, inp.split('+'))
        print(a + b)
    else:
        print('skipped')
