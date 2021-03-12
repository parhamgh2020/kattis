inp = list(map(int, input().split()))
inp.sort()
dictionary = {'A': inp[0], 'B': inp[1], 'C': inp[2]}
order = ' '.join(input()).split()
for i in order:
    print(dictionary[i], end=' ')

