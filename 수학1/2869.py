import math, sys
input = sys.stdin.readline

A, B, V = map(int,input().split())
if A >= V:
    print(1)
else:
    Day = math.ceil((V-A)/(A-B)) + 1
    print(Day)