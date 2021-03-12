l, r = list(map(int, input().split()))
if l == r == 0:
    print('Not a moose')
elif l == r > 0:
    print('Even ', l * 2)
else:
    print('Odd ', max(l, r) * 2)

