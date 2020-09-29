import sys

N = int(sys.stdin.readline())
nums = sys.stdin.readline().split()
nums = list(map(int, nums))
nums.sort()

print(nums[0],nums[-1])


# 파이썬의 Asterisk(*) 이해하기
# https://mingrammer.com/understanding-the-asterisk-of-python/
# 컨테이너 타입의 데이터를 unpacking 할 때 부분 참고