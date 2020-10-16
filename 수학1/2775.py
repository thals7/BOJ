T = int(input())
for case in range(T):
    k = int(input())
    n = int(input())
    people = [i for i in range(1,n+1)]
    for floor in range(k):
        for width in range(1,n):
            people[width] += people[width-1]
    print(people[-1])
