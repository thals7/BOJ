Croa = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
Word = input()
Cnt = 0
for i in range(len(Word)):
    if Word[i:i+2] in Croa:
        if Word[i-1] == 'd':
            Cnt -= 1
            continue
        else:
            continue
    else:
        Cnt += 1
print(Cnt)

