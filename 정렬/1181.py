import sys
input = sys.stdin.readline

tmp = []; sort_lst = []

for _ in range(int(input())):
    tmp.append(input().rstrip())
lst = list(set(tmp)) # 리스트 중복 제거

for i in lst:
    sort_lst.append((len(i),i))
sort_lst.sort()

for j in sort_lst:
    print(j[1])