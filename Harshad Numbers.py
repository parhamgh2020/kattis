number = int(input())
number_sum = sum(map(int, (' '.join(str(number)).split())))
while number % number_sum != 0:
    number += 1
    number_sum = sum(map(int, (' '.join(str(number)).split())))

print(number)
