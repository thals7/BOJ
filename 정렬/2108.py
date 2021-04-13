import sys
num_dict = dict()
num_list = []

n = int(sys.stdin.readline())
for _ in range(n):
    num = int(sys.stdin.readline())
    num_list.append(num)
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1

# 정렬 (퀵소트)
def quicksort(list):
    if len(list) <= 1:
        return list
    pivot = list[len(list)//2]
    left, right, same = [], [], []
    for i in list:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            same.append(i)
    return quicksort(left) + same + quicksort(right)

sorted_list = quicksort(num_list)

# 1. 산술평균
total = 0
for i in sorted_list:
    total += i
print(round(total/n))

# 2. 중앙값
print(sorted_list[n//2])

# 3. 최빈값
sorted_dict = sorted(num_dict.items())
sorted_dict.sort(key=lambda x:x[1], reverse=True)

if len(sorted_dict) == 1 or sorted_dict[0][1] != sorted_dict[1][1]:
    print(sorted_dict[0][0])
else:
    print(sorted_dict[1][0])

# 4. 범위
print(sorted_list[-1]-sorted_list[0])
