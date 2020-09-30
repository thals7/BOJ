N = int(input())
Cases = [input() for _ in range(N)]

for case in Cases:
    count = 0
    score = []
    for i in list(case):
        if i == 'O':
            count += 1
        elif i == 'X':
            count = 0
        score.append(count)
    print(sum(score))
