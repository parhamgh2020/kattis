n, m = map(int, input().split())
s = set()
for _ in range(m):
    s.add(int(input()))
for i in range(n):
    if i not in s:
        print(i)
print(f'Mario got {len(s)} of the dangerous obstacles.')


