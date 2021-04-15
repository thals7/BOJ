import sys

# 1. 처음 풀이
croa = list(sys.stdin.readline().rstrip())
cnt = 0

for i in range(len(croa)):
    cnt += 1
    if croa[i] == '=':
        if i > 1 and croa[i-1] == 'z' and croa[i-2] == 'd':
            cnt -= 2
        else:
            cnt -= 1
    elif croa[i] == '-':
        cnt -= 1
    elif i > 0 and croa[i] == 'j':
        if croa[i-1] == 'l' or croa[i-1] == 'n':
            cnt -= 1

print(cnt)


# 2. replace 함수 활용
word = sys.stdin.readline().rstrip()
croa = ['c=','c-','d-','dz=','lj','nj','s=','z=']

for i in croa:
    word = word.replace(i,' ')
print(len(word))