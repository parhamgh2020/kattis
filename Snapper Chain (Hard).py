T = int(input())
for i in range(1, T + 1):
    N, K = map(int, input().split())
    if K > 0 and (K + 1) % 2**N == 0:
        print(f"Case #{i}: ON")
    else:
        print(f"Case #{i}: OFF")