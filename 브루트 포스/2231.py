n = int(input())
num = 0
for i in range(n-9*len(str(n)),n-len(str(n))+2):
    if i < 0: continue
    sum = i
    for j in range(len(str(i))):
        sum += int(str(i)[j:j+1])
    if sum == n:
        num = i
        break
print(num)