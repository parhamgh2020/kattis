import re
a = input()
b = input()
if a == b:
    print('Yes')
elif a.swapcase() == b:
    print('Yes')
elif re.match('/d')