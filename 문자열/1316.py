N = int(input())
count = 0
for _ in range(N):
    Word = list(str(input()))
    lst = []
    for i in Word:
        if i not in lst:
            lst.append(i)
        else:
            if lst[-1] == i:
                continue
            else:
                count += 1
                break
print(N-count)
