import sys

n, c = map(int,sys.stdin.readline().split())
house = sorted([int(sys.stdin.readline()) for _ in range(n)])

left = 1
right = house[-1]-house[0] # 맨 끝집 - 맨 앞집
ans = 0

while left <= right:
    mid = (left+right)//2 # 집 사이의 최대 거리와 최소 거리의 중간값
    cnt = 1 # 와이파이 첫번째 집에 설치
    cur = house[0]

    for i in range(1,n):
        if house[i] >= cur + mid: # 설치 간격 충족한다면
            cnt += 1 # house[i]에 와이파이 설치
            cur = house[i] # 이제 house[i]로부터 그 다음 집들간에 간격 충족하는지 확인
    if cnt >= c: # 설치된 와이파이 개수가 c보다 큰 경우
        left = mid+1 # 두 공유기 사이의 거리가 지금보다 더 커져도 됨
        ans = mid # while문 종료될 수도 있으므로 그 전에 값 저장
    else: # 설치된 와이파이 개수가 c보다 적은 경우
        right = mid-1 # 두 공유기 사이의 거리가 지금보다 작아져야 함

print(ans)