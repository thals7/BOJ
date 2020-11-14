n = str(input())
lst = [n[i] for i in range(len(n))]
print(''.join(sorted(lst,reverse=True)))