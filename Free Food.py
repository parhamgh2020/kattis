days_in_year = []
days_in_charity = set()
for i in range(1, 365 + 1):
    days_in_year.append(i)

for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    for i in range(a, b + 1):
        days_in_charity.add(i)

print(len(days_in_charity))
