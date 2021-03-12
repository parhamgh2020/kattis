for t in range(int(input())):
    row, column = pixel = tuple(map(int, input().split()))
    pic = list()
    for _ in range(row):
        pic.append(input())
    for i in range(len(pic)):
        pic[i] = pic[i][::-1]
    pic = pic[::-1]
    print(f'Test {format(t + 1)}')
    for i in pic:
        print(i)
