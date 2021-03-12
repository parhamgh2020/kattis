num = input()
smallest = int(''.join(sorted(num)))
biggest = int(''.join(sorted(num, reverse=True)))
num = int(num)
if biggest == num:
    print(0)
else:
    while True:
        if sorted(str(smallest)) == sorted(str(num)) and smallest > num:
            print(smallest)
            break
        smallest += 1
