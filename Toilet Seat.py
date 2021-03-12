input_ = input()
D = input_[1:].count('D') * 2
U = input_[1:].count('U') * 2
if input_[0] == input_[1] == 'D':
    D -= 1
elif input_[0] == 'D' and input_[1] == 'U':
    D += 1
elif input_[0] == input_[1] == 'U':
    U -= 1
elif input_[0] == 'U' and input_[1] == 'D':
    U += 1

third = int()
for i, j in list(zip(input_[0:-1], input_[1:])):
    if i != j:
        third += 1

print(D)
print(U)
print(third)
