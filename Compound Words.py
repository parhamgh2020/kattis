w = set()

for _ in range(2):
    inp = input().split()
    for i in inp:
        w.add(i)

answer = set()
for i in w:
    for j in w:
        if i != j:
            answer.add(i + j)
for i in answer:
    print(i)
