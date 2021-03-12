x, y, n = list(map(int, input().split()))
answer = str()
for i in range(1, n + 1):
    if i % x == 0 and i % y == 0:
        answer = "FizzBuzz"
    elif i % x == 0:
        answer = "Fizz"
    elif i % y == 0:
        answer = "Buzz"
    else:
        answer = i
    print(answer)
