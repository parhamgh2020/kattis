from heapq import heappop, heappush

n_researchers, inactivity_min = map(int, input().split())
lst_arrival, lst_departure = [], []
for _ in range(n_researchers):
    arrive_at, stay_for_min = map(int, input().split())
    heappush(lst_arrival, arrive_at)
    heappush(lst_departure, arrive_at + stay_for_min)

save_min = 0
while lst_arrival:
    arrival = heappop(lst_arrival)
    while arrival - lst_departure[0] > inactivity_min:
        heappop(lst_departure)
    if lst_departure[0] <= arrival:
        heappop(lst_departure)
        save_min += 1

print(save_min)
