'''x = input()
y = int(len(x))
length = int(y/3)

words = [x[0:length], x[length:2*length], x[2*length:y]]
print(max(set(words), key = words.count))

'''