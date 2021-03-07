import sys

n = int(sys.stdin.readline())
i = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

# 회의 시작시간과 끝나는 시간이 같을 수 있으므로
# 시작시간을 기준으로 먼저 정렬한 뒤
# 끝나는 시간을 기준으로 한번 더 정렬해줌
i.sort(key=lambda x:x[0])
i.sort(key=lambda x:x[1])

last = 0
cnt = 0
for start,end in i:
    if start >= last:
        cnt += 1
        last = end

print(cnt)