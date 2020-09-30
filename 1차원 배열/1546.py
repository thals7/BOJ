import sys
input = sys.stdin.readline
N = int(input())
Score = list(map(int,input().split()))
M = max(Score)
M_Score = []

for j in Score:
    M_Score.append(int(j)/M*100)

print(sum(M_Score)/N)