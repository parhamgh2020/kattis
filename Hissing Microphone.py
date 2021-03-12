word = input()
for i in range(len(word)-1):
    if word[i] == 's':
        if word[i + 1] == 's':
            print('hiss')
            break
else:
    print('no hiss')
