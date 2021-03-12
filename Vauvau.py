aggressive_1, calm_1, aggressive_2, calm_2 = list(map(int, input().split()))
p, m, g = list(map(int, input().split()))

dog_1 = (aggressive_1, calm_1)
dog_2 = (aggressive_2, calm_2)


def is_aggressive(dog, time):
    if time > (dog[0] + dog[1]):
        if time % (dog[0] + dog[1]) <= dog[0]:
            return True
        else:
            return False
    else:
        if time <= dog[0]:
            return True
        else:
            return False


def counter(person):
    n = 0
    if is_aggressive(dog_1, person):
        n += 1
    if is_aggressive(dog_2, person):
        n += 1
    return n


def output(person):
    if counter(person) == 0 :
        print('none')
    elif counter(person) == 1:
        print('one')
    else:
        print('both')


output(p)
output(m)
output(g)