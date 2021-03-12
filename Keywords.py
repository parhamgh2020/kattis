unique_lst = set()
for _ in range(int(input())):
    inp = input().lower()
    if ' ' in inp:
        inp = inp.replace(' ', '-')
    unique_lst.add(inp)

print(len(unique_lst))