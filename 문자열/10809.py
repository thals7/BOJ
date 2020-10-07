import string
S = list(input())
Apb_list = list(string.ascii_lowercase)

for Alphabet in Apb_list:
    if S.count(Alphabet) >= 1:
        print(S.index(Alphabet), end=' ')
    else:
        print(-1, end=' ')