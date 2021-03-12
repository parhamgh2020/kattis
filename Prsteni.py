import math

n = int(input())
r = list(map(int, input().split()))
for i in range(1, n):
    gcd = math.gcd(r[0], r[i])
    print(r[0] // gcd, '/', r[i] // gcd,sep='')
