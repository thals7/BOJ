import string

Word = list(str(input()).upper())
C = []
ASCII = list(string.ascii_uppercase)
for Alphabet in ASCII:
    C.append(Word.count(Alphabet))
M = C.index(max(C))
if C.count(max(C)) > 1:
    print('?')
else:
    print(ASCII[M])