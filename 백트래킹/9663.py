import sys

input = lambda : sys.stdin.readline().rstrip()

n = int(input())
cols = [0] * n
cnt = 0


def nQueen(level):
    global cnt
    if level == n:
        cnt += 1
        return
    for i in range(n):
        cols[level] = i
        if promising(level):
            nQueen(level+1)


def promising(level):
    for i in range(level):
        # 열 및 대각선 체크
        if cols[level] == cols[i] or abs(cols[level]-cols[i]) == level-i:
            return False
    return True


nQueen(0)
print(cnt)