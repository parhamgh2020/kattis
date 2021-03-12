input_1 = input()
len_each_word = int(len(input_1) / 3)
answer = str()
for i in range(len_each_word):
    a = str()
    a += input_1[i:len(input_1): len_each_word]
    if a.count(a[0]) > 1:
        answer += a[0]
    else:
        answer += a[1]

print(answer)
