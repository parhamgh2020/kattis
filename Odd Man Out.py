for case in range(int(input())):
    input()
    numbers = input().split()
    for i in numbers:
        if numbers.count(i) == 1:
            print("Case #{}: {}".format(case + 1, i))
