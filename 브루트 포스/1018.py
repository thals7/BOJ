N, M = map(int,input().split())
# N:열 M:행
chess = [list(input()) for _ in range(N)]
cnt_list = []

for i in range(N-7): #전체 사각형 열
    for j in range(M-7): #전체 사각형 행
        cnt1 = 0 # 맨 처음 칸이 W로 시작할 때
        cnt2 = 0 # 맨 처음 칸이 B로 시작할 때
        for k in range(i,i+8):
            for l in range(j,j+8): # 8x8만큼 떼어내기
                if (k+l)%2==0: # (짝,짝),(홀,홀)인 칸에 대하여
                    if chess[k][l] != 'W': cnt1 += 1
                    if chess[k][l] != 'B': cnt2 += 1
                else: # (짝,홀),(홀,짝)인 칸에 대하여
                    if chess[k][l] != 'B': cnt1 += 1
                    if chess[k][l] != 'W': cnt2 += 1
        cnt_list.append(cnt1)
        cnt_list.append(cnt2)
print(min(cnt_list))