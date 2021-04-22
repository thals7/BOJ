import sys

n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
op = list(map(int,sys.stdin.readline().split()))
result = []


def solve(cur, idx):
    if idx == n:
        result.append(cur)
        return
    for i in range(4):
        if op[i] > 0:
            op[i] -= 1
            if i == 0:
                solve(cur + nums[idx], idx+1)
            elif i == 1:
                solve(cur - nums[idx], idx+1)
            elif i == 2:
                solve(cur * nums[idx], idx+1)
            elif i == 3:
                # 음수를 양수로 나누는 경우 양수로 바꾼 뒤 몫을 취핟고, 그 몫을 음수로 바꿈
                if cur < 0:
                    solve(-(abs(cur) // nums[idx]), idx+1)
                solve(cur // nums[idx], idx+1)
            op[i] += 1


solve(nums[0],1)
print(max(result))
print(min(result))