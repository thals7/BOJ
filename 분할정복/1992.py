import sys

n = int(sys.stdin.readline())
quad = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]

def quadtree(x,y,n):
    chk = quad[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if quad[i][j] != chk:
                print("(",end="")
                quadtree(x,y,n//2) # 왼쪽 위
                quadtree(x,y+n//2,n//2) # 오른쪽 위
                quadtree(x+n//2,y,n//2) # 왼쪽 아래
                quadtree(x+n//2,y+n//2,n//2) # 오른쪽 아래
                print(")",end="")
                return
    if chk == 0:
        print("0",end="")
        return
    else:
        print("1",end="")
        return

quadtree(0,0,n)