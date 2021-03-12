word = set(input())
letter = list(input())
# p1, p2 = True, False
i = 0
lose_p = 10
while lose_p > 0:
    if letter[i] in word:
        word.remove(letter[i])
    else:
        # p1, p2 = p2, p1
        lose_p -= 1
    if len(word) == 0:
        break
    i += 1
print('WIN' if not word else 'LOSE')
