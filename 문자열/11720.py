import sys
input = sys.stdin.readline

N = input()
N_list = map(int,list(str(input().rstrip('\n'))))
print(sum(N_list))

# sys.stdin.readline으로 문자를 입력받을시에는 맨 마지막에 \n 개행문자가 붙게 된다.
# 따라서 rstrip을 통해 \n을 제거해줘야함.