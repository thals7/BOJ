import sys

n = int(sys.stdin.readline())
p = [list(sys.stdin.readline().split()) for _ in range(n)]
ans = []

def solution(x,y,n):
    chk = p[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if chk != p[i][j]:
                solution(x,y,n//3)
                solution(x,y+n//3,n//3)
                solution(x,y+2*n//3,n//3)
                solution(x+n//3,y,n//3)
                solution(x+n//3,y+n//3,n//3)
                solution(x+n//3,y+2*n//3,n//3)
                solution(x+2*n//3,y,n//3)
                solution(x+2*n//3,y+n//3,n//3)
                solution(x+2*n//3,y+2*n//3,n//3)
                return
    if chk == "-1":
        ans.append(-1)
    elif chk == "0":
        ans.append(0)
    elif chk == "1":
        ans.append(1)

solution(0,0,n)
print(ans.count(-1))
print(ans.count(0))
print(ans.count(1))