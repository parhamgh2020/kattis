line_1 = list(map(int, input().split()))  # [0] start time , [1] class time , [2] transit routes
line_2 = list(map(int, input().split()))  #
line_3 = list(map(int, input().split()))
line_4 = list(map(int, input().split()))  # arrival

sum_time = line_1[0]
for i in range(line_1[2]):
    sum_time += line_2[i]
    if sum_time > line_4[i]:
        sum_time += (sum_time % line_4[i]) + line_3[i]
    else:
        sum_time += (line_4[i] - sum_time) + line_3[i]

sum_time += line_2[-1]
if sum_time < line_1[1]:
    print("yes")
else:
    print("no")

'''
def read():
    s,t,n = map(int,input().split())
    walks = list(map(int, input().split()))
    drives = list(map(int, input().split()))
    arrivals = list(map(int, input().split()))
    return s,t,n,walks,drives,arrivals

def on_time(s,t,n,walks,drives,arrivals):
    for _ in range(n):
        s += walks.pop(0)
        s += (lambda a: (a-(s%a))%a)(arrivals.pop(0))
        s += drives.pop(0)
        if s > t:
            return False
    return s + walks.pop() <= t

def main():
    print('yes' if on_time(*read()) else 'no')

if __name__ == "__main__":
    main()'''
