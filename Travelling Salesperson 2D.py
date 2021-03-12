from math import sqrt


def euclidean_dis(a, b):
    return sqrt(a ** 2 - b ** 2)


def greedy_tour(n):
    tour, used = [], []
    tour[0] = 0
    used[0] = True
    for i in range(1, n):
        best = -1
        for j in range(0, n):
            if not used[j] and (best == -1 or euclidean_dis(tour[i - 1], j) < euclidean_dis(tour[i - 1], best)):
                best = j
            tour[i] = best
            used[best] = True
        return tour


n = int(input())
for _ in range(n):
    a, b = map(int, input().split())

'''
GreedyTour
   tour[0] = 0
   used[0] = true
   for i = 1 to n-1
      best = -1
      for j = 0 to n-1
         if not used[j] and (best = -1 or dist(tour[i-1],j) < dist(tour[i-1],best))
            best = j
      tour[i] = best
      used[best] = true
   return tour'''
