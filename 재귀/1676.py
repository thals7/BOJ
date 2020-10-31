def fac(num):
    if num == 0: return 1
    else: return fac(num-1)*num

factorial = str(fac(int(input())))
f_lst = []
for i in factorial:
    f_lst.append(i)
f_lst.reverse()
for j in f_lst:
    if j == '0': continue
    elif j != '0':
        print(f_lst.index(j))
        break