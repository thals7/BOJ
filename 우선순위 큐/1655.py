import sys
import heapq

n = int(sys.stdin.readline())
# 중간값을 기준으로 왼쪽은 max_heap, 오른쪽은 min_heap으로 구성
# 중간값은 항상 max_heap의 맨 첫번째 값이 되도록 함
max_heap = []
min_heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-num,num)) # heapq에서 최대힙은 튜플을 구성하여 튜플 내에서 맨 앞에 있는 값을 기준으로 최소힙이 구성되는 원리를 이용
    else:
        heapq.heappush(min_heap, (num,num))

    # 만약 왼쪽 max_heap의 첫번째 원소가 오른쪽 min_heap의 첫번째 원소보다 크면
    # 오른쪽과 왼쪽의 원소값을 change
    if min_heap and max_heap[0][1] > min_heap[0][1]:
        left = heapq.heappop(max_heap)[1]
        right = heapq.heappop(min_heap)[1]
        heapq.heappush(min_heap, (left, left))
        heapq.heappush(max_heap, (-right, right))

    print(max_heap[0][1])
