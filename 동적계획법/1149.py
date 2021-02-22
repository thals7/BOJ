import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
rgb = []
rgb.append(list(map(int,input().split())))


for i in range(1,n):
    rgb.append(list(map(int,input().split())))
    rgb[i][0] = min(rgb[i - 1][1], rgb[i - 1][2]) + rgb[i][0]
    rgb[i][1] = min(rgb[i - 1][0], rgb[i - 1][2]) + rgb[i][1]
    rgb[i][2] = min(rgb[i - 1][0], rgb[i - 1][1]) + rgb[i][2]
print(min(rgb[n-1]))