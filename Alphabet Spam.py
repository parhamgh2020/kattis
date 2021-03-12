# for i in range(33, 126 + 1):
#     print(i,' = ',chr(i))
w = whitespace = int()
s = symbol = int()
l = lowercase = int()
u = uppercase = int()
input_1 = input()
t = int(len(input_1))
for i in input_1:
    if i.islower():
        l += 1
    elif i.isupper():
        u += 1
    elif i == '_':
        w += 1
    else:
        s += 1

print(w / t)
print(l / t)
print(u / t)
print(s / t)
