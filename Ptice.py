participant = ['Adrian', 'Bruno', 'Goran']
sequence = ['ABC', 'BABC', 'CCAABB']
score = [0, 0, 0]
n = int(input())
test = input()
for p in range(3):
    for t in range(len(test)):
        if test[t] == sequence[p][t % len(sequence[p])]:
            score[p] += 1

high_score = max(score)
print(high_score)
for i in range(len(score)):
    if score[i] == high_score:
        print(participant[i])
