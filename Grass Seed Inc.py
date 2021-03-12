cost = float(input())
overall_cost = 0
for _ in range(int(input())):
    w, l = list(map(float, input().split()))
    overall_cost += w * l * cost

print(format(overall_cost, " .6f"))
