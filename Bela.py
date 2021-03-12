hands, suit = input().split()
number = ('A', 'K', 'Q', 'J', 'T', '9', '8', '7')
dominant = (11, 4, 3, 20, 10, 14, 0, 0)
not_dominant = (11, 4, 3, 2, 10, 0, 0, 0)
output_1 = int()

for i in range(int(hands) * 4):
    input_1 = input()
    if input_1[1] == suit:
        output_1 += dominant[number.index(input_1[0])]
    else:
        output_1 += not_dominant[number.index(input_1[0])]

print(output_1)