import sys

while True:
    try:
        num = sys.stdin.readline().split()
        A = int(num[0])
        B = int(num[1])
        print(A+B)
    except:
        break

# 이 문제의 목적은 파일의 끝(EOF)을 올바르게 판단하는 법을 연습하는 것임.
# 더 이상 읽을 게 없을 때 프로그램을 종료하는 방법을 알아야 함
# 파이썬의 경우 예외처리를 통해서 입력값이 들어오지 않을때 프로그램을 종료할 수 있음