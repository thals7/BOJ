# n log n
import sys

n = int(sys.stdin.readline())
num = sorted(map(int,list(sys.stdin.readline() for _ in range(n))))
for i in num:
    print(i)

# 힙소트 시간초과 ??
def heapify(list, index, size):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    if left < size and list[left] > list[largest]:
        largest = left
    if right < size and list[right] > list[largest]:
        largest = right
    if largest != index:
        list[largest], list[index] = list[index], list[largest]
        heapify(list, largest, size)

def heap_sort(list):
    n = len(list)
    for i in range(n//2-1, -1, -1):
        heapify(list, i, n)
    for i in range(n-1, 0, -1):
        list[0], list[i] = list[i], list[0]
        heapify(list, 0, i)
    return list

lst = heap_sort(num)
print('\n'.join(lst))
