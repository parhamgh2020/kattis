for _ in range(int(input())):
    b, p = input().split()
    b = int(b)
    p = float(p)
    bpm = 60 * b / p
    bpm_min = bpm - (bpm / b)
    bpm_max = bpm + (bpm / b)
    print(f"{format(bpm_min, ' .4f')} {format(bpm, ' .4f')} {format(bpm_max, ' .4f')}")
