lst = list()

for _ in range(int(input())):
    lst.append(list(map(int, input().split())))

for i in lst:
    r, e, c = i
    revenue, advertise = bool(), bool()
    if r > 0:
        revenue = True
    if e > 0:
        advertise = True
    if c > e:
        advertise = False

    if revenue and advertise:
        print('does not matter')
    elif revenue == False and advertise == False:
        print('do not advertise')
    elif revenue == False and advertise == True:
        print('advertise')
    else:
        print('does not matter')
