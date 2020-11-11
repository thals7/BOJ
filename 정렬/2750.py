n = int(input()); lst = []
for _ in range(n):
    lst.append(int(input()))

# list.sort() 방식
lst.sort()

# 삽입 정렬
for i in range(1, len(lst)):
    while i>0 and lst[i] < lst[i-1]:
        lst[i], lst[i-1] = lst[i-1], lst[i]
        i -= 1

# 버블 정렬
for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

for j in lst:
    print(j)