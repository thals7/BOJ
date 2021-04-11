import sys

n = int(sys.stdin.readline())

five = 0
three = 0

while n > 0:
    if n % 5 == 0:
        five += n // 5
        break
    three += 1
    n -= 3

if n < 0:
    print(-1)
else:
    print(five+three)