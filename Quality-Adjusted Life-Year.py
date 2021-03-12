# lst = list
# for i in range(int(input())):
#     lst.append(list(map(float, input().split())))
# print(lst)
# a = abs(0 - lst[-1][1]) /(abs(lst[-1][1] - lst[-2][1]) / abs(lst[-1][2] - lst[-2][2]))
# answer = a + lst[-1][2]

# print('%.3f' % sum((lambda z: float(z[0])*float(z[1]))(input().split()) for _ in range(int(input()))))

c = float()
for i in range(int(input())):
    a, b = map(float, input().split())
    c += a * b

print('{}'.format(c, '.3f'))
