import sys
input = sys.stdin.readline
n = int(input()); lst = []
for _ in range(n):
    lst.append(tuple(map(int,input().split())))
sys.stdout.write('\n'.join(f'{i[0]} {i[1]}' for i in sorted(lst)))
