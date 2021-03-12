# Gunnar = map(int, input().split())
# Emma = map(int, input().split())
def counter():
    a1, b1, a2, b2 = map(int, input().split())
    return ((a1 + a2) / 2) + ((b1 + b2) / 2)


Gunner = counter()
Emma = counter()
if Gunner > Emma:
    print('Gunnar')
elif Emma > Gunner:
    print('Emma')
elif Gunner == Emma:
    print('Tie')
else:
    None
