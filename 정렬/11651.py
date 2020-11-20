import sys
input = sys.stdin.readline
n = int(input()); lst = []
for _ in range(n):
    x,y = map(int,input().split())
    lst.append((y,x))
sys.stdout.write('\n'.join(f'{i[1]} {i[0]}' for i in sorted(lst)))