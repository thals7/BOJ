import sys

s1 = list(sys.stdin.readline().rstrip())
s2 = list(sys.stdin.readline().rstrip())


# 1. Bottom-Up 방식
dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]

# 0부터 시작할 경우 i=0이고 문자가 같을때 i-1이 -1이 되어버리므로 1부터 시작 (대신 s1, s2는 0부터 시작하므로 i-1,j-1 번째 인덱스를 비교해줘야됨)
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        # i-1번째 문자와 j-1번째 문자가 같을때
        if s1[i-1] == s2[j-1]:
            # 대각선 위의 dp에 +1한 값으로 갱신
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])


# 1-1. 더 간단하게 구현
dp = [0] * len(s2)

for i in range(len(s1)):
    LCS = 0
    for j in range(len(s2)):
        if LCS < dp[j]:
            LCS = dp[j]
        elif s1[i] == s2[j]:
            dp[j] = LCS + 1

print(max(dp))


# 2. Top-down 방식 (재귀 이용) -> 런타임 에러
dp = [[0]*len(s2) for _ in range(len(s1))]

def LCS(x,y):
    if x == -1 or y == -1:
        return 0

    if s1[x] == s2[y]:
        dp[x][y] = LCS(x-1,y-1) + 1
    else:
        dp[x][y] = max(LCS(x-1,y), LCS(x,y-1))

    return dp[x][y]

print(LCS(len(s1)-1,len(s2)-1))