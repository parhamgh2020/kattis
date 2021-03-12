num = int(input())
if num % 4 == 0:
    print('Even')
else:
    print('Odd' if num % 4 == 2 else 'Either')
