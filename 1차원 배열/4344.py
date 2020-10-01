import sys
input = sys.stdin.readline

C = int(input())

for i in range(C):
    count = 0
    N, *Score = map(int,input().split())
    for j in Score:
        if int(j) > sum(Score)/N:
            count += 1
    print("{}%".format(format(count/N*100,".3f")))