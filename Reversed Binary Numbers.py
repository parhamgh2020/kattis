a = format(int(input()), 'b')
dec = int()
for i in range(len(a)):
    dec = dec + (int(a[i]) * pow(2, i))

print(dec)
