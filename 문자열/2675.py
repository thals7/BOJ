import sys
input = sys.stdin.readline

T = int(input())
for Case in range(T):
    R, S = input().split()
    for String in list(S):
        print(String*int(R), end='')
    print()