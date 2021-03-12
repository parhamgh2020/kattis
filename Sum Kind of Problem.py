for _ in range(int(input())):
    k, n = map(int, input().split())
    sum_, sum_odd, sum_even = 0, 0, 0
    for i in range(1, n + 1):
        sum_ += i
        sum_odd += (i * 2) - 1
        sum_even += (i * 2)
    print(k, sum_, sum_odd, sum_even, sep=' ')
