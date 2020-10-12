Croa = ['c=', 'c-', 'dz', 'd-', 'lj', 'nj', 's=', 'z=']
Word = str(input())
Cnt = 0
for i in range(len(Word)):
    print(Word[i:i+2])
    if Word[i:i+2] in Croa:
        if i <= len(Word)-3:
            if Word[i:i+2] == 'dz' and Word[i+2] != '=':
                Cnt += 1
        else:
            continue
    else:
        Cnt += 1
print(Cnt)
