for _ in range(int(input())):
    number = input()
    sum_num = int()
    for i in range(len(number)):
        if i % 2 == 0:
            a = int(number[i]) * 2
            if len(str(a)) > 1:
                for j in str(a):
                    sum_num += int(j)
            else:
                sum_num += a
        else:
            sum_num += int(number[i])
    print(sum_num)
    if sum_num % 10 == 0:
        print('PASS')
    else:
        print('FAIL')
