class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def max_point(points):
    n = len(points)
    result = 0
    for i in range(n):
        dct_map = {}
        same, vertical = 1, 0
        slope_max = 0
        for j in range(i + 1, n):
            dx = points[i].x - points[j].x
            dy = points[i].x - points[j].y
            if dx == dy == 0:
                same += 1
            elif dx == 0:
                vertical += 1
            else:
                slope = float(dy) / float(dx)
                dct_map[slope] = dct_map.get(slope, 0) + 1
                slope_max = max(slope_max, dct_map[slope])
            result = max(result, max(slope_max, vertical) + same)
        if n == 1:
            return 1
        return result


while True:
    n = int(input())
    points = []
    if n == 0:
        break
    for _ in range(n):
        x, y = map(int, input().split())
        points.append(Point(x, y))
    print(max_point(points))
