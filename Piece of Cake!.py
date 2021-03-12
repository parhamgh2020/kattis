length, horizontal, vertical = lst = list(map(int, input().split()))
height = 4

if length - horizontal > horizontal:
    horizontal = length -horizontal
if length - vertical > vertical:
    vertical = length - vertical

print(horizontal * vertical * height)

